"""IPython notebook API for Otter Check"""

import datetime as dt
import inspect
import json
import os
import pickle
import re
import time
import warnings
import zipfile

from getpass import getpass
from glob import glob
from IPython import get_ipython
from IPython.display import display, HTML, Javascript
from textwrap import indent
from urllib.parse import urljoin

from .logs import LogEntry, EventType, Log
from .utils import colab_incompatible, grade_zip_file, logs_event, running_on_colab, save_notebook

from ..execute import check
from ..export import export_notebook
from ..plugins import PluginCollection
from ..test_files import GradingResults
from ..test_files.metadata_test import NOTEBOOK_METADATA_KEY


_OTTER_LOG_FILENAME = ".OTTER_LOG"
_SHELVE = False
_ZIP_NAME_FILENAME = "__zip_filename__"


class Notebook:
    """
    Notebook class for in-notebook autograding

    Args:
        nb_path(``str``, optional): path to the notebook being run
        tests_dir (``str``, optional): path to tests directory
        colab (``bool``, optional): whether this notebook is being run on Google Colab; if ``None``,
            this information is automatically parsed from IPython on creation
    """

    # overrides tests_dir arg in __init__, used for changing tests dir during grading
    _tests_dir_override = None

    @logs_event(EventType.INIT)
    def __init__(self, nb_path=None, tests_dir="./tests", colab=None):
        global _SHELVE

        if colab is None:
            colab = running_on_colab()

        if colab and not os.path.isdir(tests_dir):
            raise ValueError(f"Tests directory {tests_dir} does not exist")

        if type(self)._tests_dir_override is not None:
            self._path = type(self)._tests_dir_override
        else:
            self._path = tests_dir

        self._colab = colab
        self._notebook = nb_path
        self._addl_files = []
        self._plugin_collections = {}

        # assume using otter service if there is a .otter file
        otter_configs = glob("*.otter")
        if otter_configs:
            # check that there is only 1 config
            assert len(otter_configs) == 1, "More than 1 otter config file found"

            # load in config file
            with open(otter_configs[0], encoding="utf-8") as f:
                self._config = json.load(f)

            _SHELVE = self._config.get("save_environment", False)
            self._ignore_modules = self._config.get("ignore_modules", [])
            self._vars_to_store = self._config.get("variables", None)

            self._notebook = self._config["notebook"]

    def _log_event(self, event_type, results=[], question=None, success=True, error=None, shelve_env={}):
        """
        Logs an event

        Args:
            event_type (``otter.logs.EventType``): the type of event
            results (``list[otter.test_files.abstract_test.TestFile]``, optional):
                the results of any checks recorded by the entry
            question (``str``, optional): the question name for this check
            success (``bool``, optional): whether the operation was successful
            error (``Exception``, optional): the exception thrown by the operation, if applicable
        """
        entry = LogEntry(
            event_type,
            results=results,
            question=question,
            success=success,
            error=error
        )

        if _SHELVE and event_type == EventType.CHECK:
            entry.shelve(
                shelve_env,
                delete=True,
                filename=_OTTER_LOG_FILENAME,
                ignore_modules=self._ignore_modules,
                variables=self._vars_to_store
            )

        entry.flush_to_file(_OTTER_LOG_FILENAME)

    def _resolve_nb_path(self, nb_path):
        """
        Attempts to resolve the path to the notebook being run. If ``nb_path`` is ``None``, ``self._notebook``
        is checked, then the working directory is searched for ``.ipynb`` files. If none are found, or 
        more than one is found, a ``ValueError`` is raised.

        Args:
            nb_path (``Optional[str]``): path to the notebook
        
        Returns:
            ``str``: resolved notebook path
        
        Raises:
            ``ValueError``: if no notebooks or too many notebooks are found.
        """
        if nb_path is None and self._notebook is not None:
            nb_path = self._notebook

        elif nb_path is None and glob("*.ipynb"):
            notebooks = glob("*.ipynb")
            assert len(notebooks) == 1, "nb_path not specified and > 1 notebook in working directory"
            nb_path = notebooks[0]

        elif nb_path is None:
            raise ValueError("Could not resolve notebook path")

        return nb_path

    @logs_event(EventType.CHECK)
    def check(self, question, global_env=None):
        """
        Runs tests for a specific question against a global environment. If no global environment
        is provided, the test is run against the calling frame's environment.

        Args:
            question (``str``): name of question being graded
            global_env (``dict``, optional): global environment resulting from execution of a single
                notebook

        Returns:
            ``otter.test_files.abstract_test.TestFile``: the grade for the question
        """
        if os.path.isdir(self._path) and os.path.isfile(os.path.join(self._path, question + ".py")):
            test_path = os.path.join(self._path, question + ".py")
            test_name = None

        elif self._colab:
            raise ValueError(f"Test {question} does not exist")

        else:
            test_path = self._resolve_nb_path(None)
            test_name = question

        # ensure that desired test exists
        assert os.path.isfile(test_path), "Test {} does not exist".format(question)

        # pass the correct global environment
        if global_env is None:
            global_env = inspect.currentframe().f_back.f_back.f_globals

        # run the check
        result = check(test_path, test_name, global_env)

        return question, result, global_env

    @colab_incompatible
    def run_plugin(self, plugin_name, *args, nb_path=None, **kwargs):
        """
        Runs the plugin ``plugin_name`` with the specified arguments. Use ``nb_path`` if the path
        to the notebook is not configured.

        Args:
            plugin_name (``str``): importable name of an Otter plugin that implements the 
                ``from_notebook`` hook
            *args: arguments to be passed to the plugin
            nb_path (``str``, optional): path to the notebook
            **kwargs: keyword arguments to be passed to the plugin

        """
        nb_path = self._resolve_nb_path(nb_path)
        if plugin_name in self._plugin_collections:
            pc = self._plugin_collections[plugin_name]
        else:
            pc = PluginCollection([plugin_name], nb_path, {})
            self._plugin_collections[plugin_name] = pc
        pc.run("from_notebook", *args, **kwargs)

    @colab_incompatible
    @logs_event(EventType.TO_PDF)
    def to_pdf(self, nb_path=None, filtering=True, pagebreaks=True, display_link=True, force_save=False):
        """
        Exports a notebook to a PDF using Otter Export

        Args:
            nb_path (``str``, optional): path to the notebook we want to export; will attempt to infer
                if not provided
            filtering (``bool``, optional): set true if only exporting a subset of notebook cells to PDF
            pagebreaks (``bool``, optional): if true, pagebreaks are included between questions
            display_link (``bool``, optional): whether or not to display a download link
            force_save (``bool``, optional): whether or not to display JavaScript that force-saves the
                notebook (only works in Jupyter Notebook classic, not JupyterLab)
        """
        nb_path = self._resolve_nb_path(nb_path)

        if force_save:
            saved = save_notebook(nb_path)
            if not saved:
                warnings.warn(
                    "Could not force-save notebook; the results of this call will be based on the last "
                    "saved version of this notebook."
                )

        # convert(nb_path, filtering=filtering, filter_type=filter_type)
        export_notebook(nb_path, filtering=filtering, pagebreaks=pagebreaks)

        if display_link:
            # create and display output HTML
            out_html = """
            <p>Your file has been exported. Download it by right-clicking
            <a href="{}" target="_blank">here</a> and selecting <strong>Save Link As</strong>.
            """.format(nb_path[:-5] + "pdf")

            display(HTML(out_html))
        self._log_event(EventType.TO_PDF)

    @colab_incompatible
    def add_plugin_files(self, plugin_name, *args, nb_path=None, **kwargs):
        """
        Runs the ``notebook_export`` event of the plugin ``plugin_name`` and tracks the file paths
        it returns to be included when calling ``Notebook.export``.

        Args:
            plugin_name (``str``): importable name of an Otter plugin that implements the 
                ``from_notebook`` hook
            *args: arguments to be passed to the plugin
            nb_path (``str``, optional): path to the notebook
            **kwargs: keyword arguments to be passed to the plugin        
        """
        nb_path = self._resolve_nb_path(nb_path)
        if plugin_name in self._plugin_collections:
            pc = self._plugin_collections[plugin_name]
        else:
            pc = PluginCollection([plugin_name], nb_path, {})
            self._plugin_collections[plugin_name] = pc
        addl_files = pc.run("notebook_export", *args, **kwargs)[0]
        if addl_files is None:
            return
        self._addl_files.extend(addl_files)

    @colab_incompatible
    @logs_event(EventType.END_EXPORT)
    def export(self, nb_path=None, export_path=None, pdf=True, filtering=True, pagebreaks=True, files=[], 
            display_link=True, force_save=False, run_tests=False):
        """
        Exports a submission to a zip file. Creates a submission zipfile from a notebook at ``nb_path``,
        optionally including a PDF export of the notebook and any files in ``files``.

        Args:
            nb_path (``str``, optional): path to the notebook we want to export; will attempt to infer
                if not provided
            export_path (``str``, optional): path at which to write zipfile; defaults to notebook's
                name + ``.zip``
            pdf (``bool``, optional): whether a PDF should be included
            filtering (``bool``, optional): whether the PDF should be filtered; ignored if ``pdf`` is
                ``False``
            pagebreaks (``bool``, optional): whether pagebreaks should be included between questions
                in the PDF
            files (``list`` of ``str``, optional): paths to other files to include in the zip file
            display_link (``bool``, optional): whether or not to display a download link
            force_save (``bool``, optional): whether or not to display JavaScript that force-saves the
                notebook (only works in Jupyter Notebook classic, not JupyterLab)
        """
        self._log_event(EventType.BEGIN_EXPORT)

        nb_path = self._resolve_nb_path(nb_path)

        if force_save:
            saved = save_notebook(nb_path)
            if not saved:
                warnings.warn(
                    "Could not force-save notebook; the results of this call will be based on the last "
                    "saved version of this notebook."
                )

        try:
            with open(nb_path) as f:
                assert len(f.read().strip()) > 0, \
                    f"Notebook {nb_path} is empty. Please save and checkpoint your notebook and rerun this cell."

        except UnicodeDecodeError:
            with open(nb_path, "r", encoding="utf-8") as f:
                assert len(f.read().strip()) > 0, \
                    f"Notebook {nb_path} is empty. Please save and checkpoint your notebook and rerun this cell."

        timestamp = dt.datetime.now().strftime("%Y_%m_%dT%H_%M_%S_%f")
        if export_path is None:
            zip_path = ".".join(nb_path.split(".")[:-1]) + "_" + timestamp + ".zip"
        else:
            zip_path = export_path

        zf = zipfile.ZipFile(zip_path, mode="w")
        zf.write(nb_path)

        if pdf:
            pdf_path = ".".join(nb_path.split(".")[:-1]) + ".pdf"
            # convert(nb_path, filtering=filtering, filter_type=filter_type)
            export_notebook(nb_path, filtering=filtering, pagebreaks=pagebreaks)
            if os.path.isfile(pdf_path):
                zf.write(pdf_path)
            else:
                warnings.warn("Could not locate a PDF to include")

        if os.path.isfile(_OTTER_LOG_FILENAME):
            zf.write(_OTTER_LOG_FILENAME)

        zf.writestr(_ZIP_NAME_FILENAME, os.path.basename(zip_path))

        if glob("*.otter"):
            assert len(glob("*.otter")) == 1, "Too many .otter files (max 1 allowed)"
            zf.write(glob("*.otter")[0])

        for file in files:
            zf.write(file)
        
        for file in self._addl_files:
            zf.write(file)

        zf.close()

        if run_tests:
            print("Running your submission against local test cases...\n")
            results = grade_zip_file(zip_path, nb_path, self._path)
            print(
                "Your submission received the following results when run against " + \
                "available test cases:\n\n" + indent(results.summary(), "    ")
            )

        if display_link:
            # create and display output HTML
            out_html = """
            <p>Your submission has been exported. Click <a href="{}" download="{}" target="_blank">here</a>
            to download the zip file.</p>
            """.format(zip_path, zip_path)

            display(HTML(out_html))

    @logs_event(EventType.END_CHECK_ALL)
    def check_all(self):
        """
        Runs all tests on this notebook. Tests are run against the current global environment, so any
        tests with variable name collisions will fail.
        """
        # TODO: this should use functions in execute.py to run tests in-sequence so that variable
        # name collisions are accounted for
        self._log_event(EventType.BEGIN_CHECK_ALL)

        # TODO: this is a janky way of resolving where the tests are. Formalize a method of 
        # determining this and put it into a method in e.g. utils.py
        tests = [os.path.split(file)[1][:-3] for file in glob(os.path.join(self._path, "*.py")) \
            if "__init__.py" not in file]
        if len(tests) == 0:
            nb_path = self._resolve_nb_path(None)
            with open(nb_path, encoding="utf-8") as f:
                nb = json.load(f)
            tests = list(nb["metadata"][NOTEBOOK_METADATA_KEY]["tests"].keys())

        global_env = inspect.currentframe().f_back.f_back.f_globals
        results = []
        if not _SHELVE:
            for test_name in sorted(tests):
                results.append(self.check(test_name, global_env))
        else:
            log = Log.from_file(_OTTER_LOG_FILENAME, ascending=False)
            for file in sorted(tests):
                if "__init__.py" not in file:
                    test_name = os.path.splitext(os.path.split(file)[1])[0]

                    entry = log.get_question_entry(test_name)
                    env = entry.unshelve()
                    global_env.update(env)
                    del locals()["env"]

                    result = self.check(test_name, global_env)
                    results.append((test_name, result))

        return GradingResults(results)
