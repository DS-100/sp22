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


def make_line_plot(df_dict, x_col, y_col, include=None, title=None, xlabel=None, ylabel=None, legend=True):
    """
    Plot a line plot of two columns for each dataframe in `df_dict`.
    
    Uses `sns.lineplot` to plot a line plot of two columns for each
    dataframe in `df_dict`. The keys of `df_dict` are used as entries in
    the legend when `legend` is `True`.
    
    Parameters
    ----------
        df_dict: dict[str: pd.DataFrame]
            a dictionary mapping handles to dataframes with the data to plot
        x_col: str
            the name of a column in each dataframe in `df_dict` to plot on
            the x-axis
        y_col: str
            the name of a column in each dataframe in `df_dict` to plot on
            the y-axis
        include: list[str], optional
            a list of handles to include in the plot; all keys in `df_dict` not 
            present in `include`, if specified, will *not* be included in the plot
        title: str, optional
            a title for the plot
        xlabel: str, optional
            a label for the x-axis; if unspecified, `x_col` is used
        ylabel: str, optional
            a label for the y-axis; if unspecified, `y_col` is used
        legend: bool, optional
            whether to include a legend with each key in `df_dict`
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    if include is not None:
        df_dict = {k: v for k, v in df_dict.items() if k in include}

    plt.figure(figsize=[10,6])
    for handle, df in df_dict.items():
        sns.lineplot(x=x_col, y=y_col, data=df, label=handle)
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if not legend:
        plt.gca().get_legend().remove()


def make_scatter_plot(df_dict, x_col, y_col, hue=None, include=None, title=None, xlabel=None, ylabel=None, 
                      legend=True, alpha=1):
    """
    Plot a scatter plot of two columns for each dataframe in `df_dict`.
    
    Uses `sns.scatterplot` to plot a scatter plot of two columns for each
    dataframe in `df_dict`. Supports grouping by color within each dataframe
    using the `hue` parameter. The keys of `df_dict` are used as entries in
    the legend when `legend` is `True`.
    
    Parameters
    ----------
        df_dict: dict[str: pd.DataFrame]
            a dictionary mapping handles to dataframes with the data to plot
        x_col: str
            the name of a column in each dataframe in `df_dict` to plot on
            the x-axis
        y_col: str
            the name of a column in each dataframe in `df_dict` to plot on
            the y-axis
        hue: str, optional
            the name of a column in each dataframe in `df_dict` to use to determine
            point color on the plot
        include: list[str], optional
            a list of handles to include in the plot; all keys in `df_dict` not 
            present in `include`, if specified, will *not* be included in the plot
        title: str, optional
            a title for the plot
        xlabel: str, optional
            a label for the x-axis; if unspecified, `x_col` is used
        ylabel: str, optional
            a label for the y-axis; if unspecified, `y_col` is used
        legend: bool, optional
            whether to include a legend with each key in `df_dict`
        alpha: float, optional
            the opacity of the points on the plot; a value on the interval [0, 1]
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    if include is not None:
        df_dict = {k: v for k, v in df_dict.items() if k in include}

    plt.figure(figsize=[10,6])
    for handle, df in df_dict.items():
        sns.scatterplot(x=x_col, y=y_col, data=df, hue=hue, label=handle, alpha=alpha)
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if not legend:
        plt.gca().get_legend().remove()
        

def make_bar_plot(counts_df, title=None, xlabel=None, ylabel=None, ylog=False, legend=True):
    """
    Plot a side-by-side bar plot of each column in `counts_df`.
    
    Uses `pd.DataFrame.plot.bar` to plot a side-by-side bar plot of
    each column of `counts_df`. The index of `counts_df` should be the 
    categories to use on the x-axis and each column should have a value 
    corresponding to the height of the bar.
    
    Parameters
    ----------
        counts_df: pd.DataFrame
            a dataframe whose index is the x-axis and whose column values are 
            the heights of the bars in each group
        title: str, optional
            a title for the plot
        xlabel: str, optional
            a label for the x-axis
        ylabel: str, optional
            a label for the y-axis
        ylog: bool, optional
            whether to plot the y-axis on a log scale
        legend: bool, optional
            whether to include a legend with each key in `df_dict`
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    counts_df.plot.bar(figsize=(15, 5))
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if ylog:
        plt.yscale("log")
    if legend:
        plt.legend()


def make_histogram(df_dict, column_name, include=None, title=None, xlabel=None, ylabel=None, legend=True, 
                   **kwargs):
    """
    Plot a histogram of a column of each dataframe in `df_dict`.
    
    Uses `sns.histplot` to plot a histogram of data for each dataframe in `df_dict`. 
    The keys of the dataframe are used as entries in the legend. Additional keyword
    arguments are passed to `sns.histplot`.
    
    Parameters
    ----------
        df_dict: dict[str: pd.DataFrame]
            a dictionary mapping handles to dataframes with the data to plot
        column_name: str
            the name of a column in each dataframe in `df_dict` to plot the 
            distribution of
        include: list[str], optional
            a list of handles to include in the plot; all keys in `df_dict` not 
            present in `include`, if specified, will *not* be included in the plot
        title: str, optional
            a title for the plot
        xlabel: str, optional
            a label for the x-axis; if unspecified, `column_name` is used
        ylabel: str, optional
            a label for the y-axis
        legend: bool, optional
            whether to include a legend with each key in `df_dict`
        **kwargs
            additional keyword arguments passed to sns.histplot (see
            https://seaborn.pydata.org/generated/seaborn.histplot.html)
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    if include is not None:
        df_dict = {k: v for k, v in df_dict.items() if k in include}
    plt.figure(figsize=[10,6])
    for color, (handle, df) in zip(sns.color_palette(), df_dict.items()):
        sns.histplot(df[column_name], color=color, label=handle, **kwargs)
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    else:
        plt.xlabel(column_name)
    if ylabel:
        plt.ylabel(ylabel)
    if legend:
        plt.legend()