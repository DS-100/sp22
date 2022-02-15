"""Some common utilities for classwork and homework in Berkeley's Data100.
"""


def head(filename, lines=5):
    """
    Returns the first few lines of a file.
    
    filename: the name of the file to open
    lines: the number of lines to include
    
    return: A list of the first few lines from the file.
    """
    from itertools import islice
    with open(filename, "r") as f:
        return list(islice(f, lines))
    

def fetch_and_cache(data_url, file, data_dir="data", force=False):
    """
    Download and cache a url and return the file object.
    
    data_url: the web address to download
    file: the file in which to save the results.
    data_dir: (default="data") the location to save the data
    force: if true the file is always re-downloaded
    
    return: The pathlib.Path object representing the file.
    """

    import requests
    from hashlib import md5
    from pathlib import Path
    
    data_dir = Path(data_dir)
    data_dir.mkdir(exist_ok=True)
    file_path = data_dir/Path(file)
    # If the file already exists and we want to force a download then
    # delete the file first so that the creation date is correct.
    if force and file_path.exists():
        file_path.unlink()
    if force or not file_path.exists():
        resp = requests.get(data_url, stream=True)
        file_size = int(resp.headers.get('content-length', 0))
        step = 40
        chunk_size = file_size//step
        with file_path.open('wb') as f:
            for chunk in resp.iter_content(chunk_size): # write file in chunks
                f.write(chunk)
                step -= 1
                print('[' + '#'*(41 - step) + (step)*' ' + ']\r', end='')
        print(f"\nDownloaded {data_url.split('/')[-1]}!")
    else:
        import time
        time_downloaded = time.ctime(file_path.stat().st_ctime)
        print("Using version already downloaded:", time_downloaded)
    # Compute and print md5 hash of file, whether newly downloaded or not
    m5 = md5()
    m5.update(file_path.read_bytes())
    print(f"MD5 hash of file: {m5.hexdigest()}")
    return file_path


def line_count(file):
    """
    Computes the number of lines in a file.
    
    file: the file in which to count the lines.
    return: The number of lines in the file
    """
    with open(file, "r") as f:
        return sum(1 for line in f)
