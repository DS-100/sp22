"""Some common utilities for classwork and homework in Berkeley's Data100.
"""
import pandas as pd
import numpy as np
from joblib import dump

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

def run_linear_regression_test(
    final_model, 
    process_data_fm, 
    threshold, 
    train_data_path, 
    test_data_path, 
    is_kaggle=False, 
    is_ranking=False
):
    def rmse(predicted, actual):
        return np.sqrt(np.mean((actual - predicted)**2))

    training_data = pd.read_csv(train_data_path, index_col='Unnamed: 0')
    X_train, y_train = process_data_fm(training_data)
    if is_kaggle:
        test_data = pd.read_csv(test_data_path, index_col='Unnamed: 0')
        X_test, y_test = process_data_fm(test_data)

    final_model.fit(X_train, y_train)
    if is_kaggle:
        y_predicted = final_model.predict(X_test)
        loss = rmse(np.exp(y_predicted), np.exp(y_test))
    else:
        y_predicted = final_model.predict(X_train)
        loss = rmse(np.exp(y_predicted), np.exp(y_train))
    if is_ranking:
        print('Your RMSE loss is: {}'.format(loss))
        return loss
    return loss < threshold
