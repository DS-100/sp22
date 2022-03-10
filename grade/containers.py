"""Docker container management for Otter Grade"""
import glob
import os
import pandas as pd
import pickle
import pkg_resources
import shutil
import tempfile

from concurrent.futures import ThreadPoolExecutor, wait
from python_on_whales import docker
from typing import Optional

from .utils import generate_hash, OTTER_DOCKER_IMAGE_TAG


def build_image(zip_path, base_image, tag):
    """
    Creates a grading image based on the autograder zip file and attaches a tag.

    Args:
        zip_path (``str``): path to the autograder zip file
        base_image (``str``): base Docker image to build from
        tag (``str``): tag to be added when creating the image

    Returns:
        ``str``: the tag of the newly-build Docker image
    """
    image = OTTER_DOCKER_IMAGE_TAG + ":" + tag
    dockerfile = pkg_resources.resource_filename(__name__, "Dockerfile")

    if not docker.image.exists(image):
        print(f"Building new image using {base_image} as base image")
        docker.build(".", build_args={
            "ZIPPATH": zip_path,
            "BASE_IMAGE": base_image
        }, tags=[image], file=dockerfile, load=True)

    return image


def launch_grade(zip_path, submissions_dir, verbose=False, num_containers=None, ext="ipynb", 
                 no_kill=False, output_path="./", debug=False, zips=False,
                 image="ucbdsinfra/otter-grader", pdfs=False, timeout=None, network=True):
    """
    Grades notebooks in parallel Docker containers

    This function runs ``num_containers`` Docker containers in parallel to grade the student submissions
    in ``submissions_dir`` using the autograder configuration file at ``zip_path``. It can additionally 
    generate PDFs for the parts of the assignment needing manual grading.

    Args:
        zip_path(``str``): path to zip file used to set up container
        submissions_dir (``str``): path to directory of student submissions to be graded
        verbose (``bool``, optional): whether status messages should be printed to the command line
        num_containers (``int``, optional): The number of parallel containers that will be run
        ext (``str``, optional): the submission file extension for globbing
        no_kill (``bool``, optional): whether the grading containers should be kept running after
            grading finishes
        output_path (``str``, optional): path at which to write grades CSVs copied from the container
        debug (``bool``, optional): whether to run grading in debug mode (prints grading STDOUT and STDERR
            from each container to the command line)
        zips (``bool``, optional): whether the submissions are zip files formatted from ``Notebook.export``
        image (``str``, optional): a base image to use for building Docker images
        pdfs (``bool``, optional): whether to copy PDFs out of the containers
        timeout (``int``): timeout in seconds for each container
        network (``bool``): whether to enable networking in the containers

    Returns:
        ``list`` of ``pandas.core.frame.DataFrame``: the grades returned by each container spawned during
            grading
    """
    if not num_containers:
        num_containers = 4

    pool = ThreadPoolExecutor(num_containers)
    futures = []
    img = build_image(zip_path, image, generate_hash(zip_path))

    if zips:
        pattern = "*.zip"
    else:
        pattern = f"*.{ext}"

    submissions = glob.glob(os.path.join(submissions_dir, pattern))
    pdf_dir = os.path.join(output_path, "submission_pdfs")

    for subm_path in submissions:
        futures += [
            pool.submit(
                grade_assignments,
                submission_path=subm_path,
                verbose=verbose,
                image=img,
                no_kill=no_kill,
                pdf_dir=pdf_dir,
                debug=debug,
                pdfs=pdfs,
                timeout=timeout,
                network=network,
            )
        ]

    # stop execution while containers are running
    finished_futures = wait(futures)

    # return list of dataframes
    return [df.result() for df in finished_futures[0]]


def grade_assignments(submission_path, image, verbose=False, no_kill=False, pdf_dir=None, 
                      debug=False, pdfs=False, timeout: Optional[int] = None, network=True):
    """
    Grades multiple submissions in a directory using a single docker container. If no PDF assignment is
    wanted, set all three PDF params (``unfiltered_pdfs``, ``tag_filter``, and ``html_filter``) to ``False``.

    Args:
        submission_path (``str``): path to the submission to be graded
        image (``str``): a Docker image tag to be used for grading environment
        verbose (``bool``, optional): whether status messages should be printed to the command line
        no_kill (``bool``, optional): whether the grading containers should be kept running after
            grading finishes
        pdf_dir (``str``, optional): directory in which to put notebook PDFs, if applicable
        debug (``bool``, False): whether to run grading in debug mode (prints grading STDOUT and STDERR
            from each container to the command line)
        pdfs (``bool``, optional): whether to copy PDFs out of the containers
        timeout (``int``): timeout in seconds for each container
        network (``bool``): whether to enable networking in the containers

    Returns:
        ``pandas.core.frame.DataFrame``: A dataframe of file to grades information
    """
    temp_subm_file, temp_subm_path = tempfile.mkstemp()
    shutil.copyfile(submission_path, temp_subm_path)

    results_file, results_path = tempfile.mkstemp(suffix=".pkl")
    pdf_path = None
    if pdfs:
        pdf_file, pdf_path = tempfile.mkstemp(suffix=".pdf")

    try:
        nb_basename = os.path.basename(submission_path)
        nb_name = os.path.splitext(nb_basename)[0]

        volumes = [
            (temp_subm_path, f"/autograder/submission/{nb_basename}"),
            (results_path, "/autograder/results/results.pkl")
        ]
        if pdfs:
            volumes.append((pdf_path, f"/autograder/submission/{nb_name}.pdf"))

        args = {}

        if network is not None and not network:
            args['networks'] = 'none'

        container = docker.container.run(image, command=["/autograder/run_autograder"], volumes=volumes, detach=True, **args)

        if timeout:
            import threading

            def kill_container():
                docker.container.kill(container)

            timer = threading.Timer(timeout, kill_container)
            timer.start()

        container_id = container.id[:12]
        if verbose:
            print(f"Grading {submission_path} in container {container_id}...")

        exit = docker.container.wait(container)

        if timeout:
            timer.cancel()

        if debug:
            print(docker.container.logs(container))

        if not no_kill:
            container.remove()

        if exit != 0:
            raise Exception(f"Executing '{submission_path}' in docker container failed! Exit code: {exit}")

        with open(results_path, "rb") as f:
            scores = pickle.load(f)

        scores = scores.to_dict()
        scores = {t: [scores[t]["score"]] if type(scores[t]) == dict else scores[t] for t in scores}
        scores["file"] = os.path.split(submission_path)[1]
        df = pd.DataFrame(scores)

        if pdfs:
            os.makedirs(pdf_dir, exist_ok=True)

            local_pdf_path = os.path.join(pdf_dir, f"{nb_name}.pdf")
            shutil.copy(pdf_path, local_pdf_path)

    finally:
        os.close(results_file)
        os.remove(results_path)
        os.close(temp_subm_file)
        os.remove(temp_subm_path)
        if pdfs:
            os.close(pdf_file)
            os.remove(pdf_path)

    return df
