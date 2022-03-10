"""Argument parser for Otter command-line tools"""

import click

from .assign import main as assign
from .check import main as check
from .export import main as export
from .generate import main as generate
from .grade import _ALLOWED_EXTENSIONS
from .grade import main as grade
from .run import main as run
from .version import print_version_info


@click.group(invoke_without_command=True)
@click.option("--version", is_flag=True, help="Show the version and exit")
def cli(version):
    """
    Command-line utility for Otter-Grader, a Python-based autograder for Jupyter Notebooks, 
    RMarkdown files, and Python and R scripts. For more information, see 
    https://otter-grader.readthedocs.io/.
    """
    if version:
        print_version_info(logo=True)
        return


defaults = assign.__kwdefaults__
@cli.command("assign")
@click.argument("master", type=click.Path(exists=True, dir_okay=False))
@click.argument("result", type=click.Path())
@click.option("--no-run-tests", is_flag=True, help="Do not run the tests against the autograder notebook")
@click.option("--no-pdfs", is_flag=True, help="Do not generate PDFs; overrides assignment config")
@click.option("--username", help="Gradescope username for generating a token")
@click.option("--password", help="Gradescope password for generating a token")
@click.option("--debug", is_flag=True, help="Do not ignore errors in running tests for debugging")
@click.option("--v1", is_flag=True, help="Use Otter Assign format v1 instead of v0")
def assign_cli(*args, **kwargs):
    """
    Create distribution versions of the Otter Assign formatted notebook MASTER and write the
    results to the directory RESULT, which will be created if it does not already exist.
    """
    return assign(*args, **kwargs)


defaults = check.__kwdefaults__
@cli.command("check")
@click.argument("file", type=click.Path(exists=True, dir_okay=False))
@click.option("-q", "--question", help="A specific quetsion to grade")
@click.option("-t", "--tests-path", default=defaults["tests_path"], type=click.Path(exists=True, file_okay=False), help="Path to the direcotry of test files")
@click.option("--seed", type=click.INT, help="A random seed to be executed before each cell")
def check_cli(*args, **kwargs):
	"""
	Check the Python script or Jupyter Notebook FILE against tests.
	"""
	return check(*args, **kwargs)


defaults = export.__kwdefaults__
@cli.command("export")
@click.argument("src", type=click.Path(exists=True, dir_okay=False))
@click.argument("dest", required=False, type=click.Path())
@click.option("--filtering", is_flag=True, help="Whether the PDF should be filtered")
@click.option("--pagebreaks", is_flag=True, help="Whether the PDF should have pagebreaks between questions")
@click.option("-s", "--save", is_flag=True, help="Save intermediate file(s) as well")
@click.option("-e", "--exporter", default=defaults["exporter"], type=click.Choice(["latex", "html"]), help="Type of PDF exporter to use")
@click.option("--debug", is_flag=True, help="Export in debug mode")
def export_cli(*args, **kwargs):
    """
    Export a Jupyter Notebook SRC as a PDF at DEST with optional filtering.

    If unspecified, DEST is assumed to be the basename of SRC with a .pdf extension.
    """
    return export(*args, **kwargs)


defaults = generate.__kwdefaults__
@cli.command("generate")
@click.option("-t", "--tests-path", default=defaults["tests_path"], type=click.Path(exists=True, file_okay=False), help="Path to test files")
@click.option("-o", "--output-dir", default=defaults["output_dir"], type=click.Path(exists=True, file_okay=False), help="Path to which to write zipfile")
@click.option("-c", "--config", type=click.Path(exists=True, file_okay=False), help="Path to otter configuration file; ./otter_config.json automatically checked")
@click.option("--no-config", is_flag=True, help="Disable auto-inclusion of unspecified Otter config file at ./otter_config.json")
@click.option("-r", "--requirements", type=click.Path(exists=True, file_okay=False), help="Path to requirements.txt file; ./requirements.txt automatically checked")
@click.option("--no-requirements", is_flag=True, help="Disable auto-inclusion of unespecified requirements file at ./requirements.txt")
@click.option("--overwrite-requirements", is_flag=True, help="Overwrite (rather than append to) default requirements for Gradescope; ignored if no REQUIREMENTS argument")
@click.option("-e", "--environment", type=click.Path(exists=True, file_okay=False), help="Path to environment.yml file; ./environment.yml automatically checked (overwrite)")
@click.option("--no-environment", is_flag=True, help="Disable auto-inclusion of unespecified environment file at ./environment.yml")
@click.option("-l", "--lang", default=defaults["lang"], type=click.Choice(["python", "r"], case_sensitive=False), help="Assignment programming language; defaults to Python")
@click.option("--username", help="Gradescope username for generating a token")
@click.option("--password", help="Gradescope password for generating a token")
@click.option("--token", help="Gradescope token for uploading PDFs")
@click.argument("files", nargs=-1)
def generate_cli(*args, **kwargs):
    """
    Generate a zip file to configure an Otter autograder, including FILES as support files.
    """
    return generate(*args, **kwargs)


defaults = grade.__kwdefaults__
@cli.command("grade")

# necessary path arguments
@click.option("-p", "--path", default=defaults["path"], help="Path to directory of submissions")
@click.option("-a", "--autograder", default=defaults["autograder"], help="Path to autograder zip file")
@click.option("-o", "--output-dir", default=defaults["output_dir"], help="Directory to which to write output")

# submission format arguments
@click.option("-z", "--zips", is_flag=True, help="Whether submissions are zip files from Notebook.export")
@click.option("--ext", type=click.Choice(_ALLOWED_EXTENSIONS), help="The extension to glob for submissions")

# PDF export options
@click.option("--pdfs", is_flag=True, help="Whether to copy notebook PDFs out of containers")

# other settings and optional arguments
@click.option("-v", "--verbose", is_flag=True, help="Flag for verbose output")
@click.option("--containers", type=click.INT, help="Specify number of containers to run in parallel")
@click.option("--image", default=defaults["image"], help="Custom docker image to run on")
@click.option("--no-kill", is_flag=True, help="Do not kill containers after grading")
@click.option("--debug", is_flag=True, help="Print stdout/stderr from grading for debugging")

@click.option("--prune", is_flag=True, help="Prune all of Otter's grading images")
@click.option("-f", "--force", is_flag=True, help="Force action (don't ask for confirmation)")
def grade_cli(*args, **kwargs):
    """
    Grade assignments locally using Docker containers.
    """
    return grade(*args, **kwargs)


defaults = run.__kwdefaults__
@cli.command("run")
@click.argument("submission")
@click.option("-a", "--autograder", default=defaults["autograder"], type=click.Path(exists=True, dir_okay=False), help="Path to autograder zip file")
@click.option("-o", "--output-dir", default=defaults["output_dir"], type=click.Path(exists=True, file_okay=False), help="Directory to which to write output")
@click.option("--no-logo", is_flag=True, help="Suppress Otter logo in stdout")
@click.option("--debug", is_flag=True, help="Do not ignore errors when running submission")
def run_cli(*args, **kwargs):
    """
    Run non-containerized Otter on a single submission.
    """
    return run(*args, **kwargs)
