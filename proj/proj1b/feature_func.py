import numpy as np
import pandas as pd

def remove_outliers(data, variable, lower=-np.inf, upper=np.inf):
    """
    Input:
      data (data frame): the table to be filtered
      variable (string): the column with numerical outliers
      lower (numeric): observations with values lower than this will be removed
      upper (numeric): observations with values higher than this will be removed

    Output:
      a data frame with outliers removed

    Note: This function should not change mutate the contents of data.
    """
    return data.loc[(data[variable] > lower) & (data[variable] < upper), :]

def add_total_bedrooms(data):
    """
    Input:
      data (data frame): a data frame containing at least the Description column.
    """
    with_rooms = data.copy()
    rooms_regex = r'(\d+) of which are bedrooms'
    rooms = with_rooms['Description'].str.extract(rooms_regex).astype(int)
    with_rooms['Bedrooms'] = rooms
    return with_rooms

def find_expensive_neighborhoods(data, n=3, metric=np.median):
    """
    Input:
      data (data frame): should contain at least a string-valued Neighborhood
        and a numeric 'Sale Price' column
      n (int): the number of top values desired
      metric (function): function used for aggregating the data in each neighborhood.
        for example, np.median for median prices

    Output:
      a list of the top n richest neighborhoods as measured by the metric function
    """
    neighborhoods = list(
        data
        .groupby('Neighborhood Code')['Log Sale Price']
        .aggregate(metric)
        .sort_values(ascending=False)
        .head(n)
        .index.values
    )

    # This makes sure the final list contains the generic int type used in Python3, not specific ones used in numpy.
    return [int(code) for code in neighborhoods]

def add_in_expensive_neighborhood(data, neighborhoods):
    """
    Input:
      data (data frame): a data frame containing a 'Neighborhood Code' column with values
        found in the codebook
      neighborhoods (list of strings): strings should be the names of neighborhoods
        pre-identified as rich
    Output:
      data frame identical to the input with the addition of a binary
      in_rich_neighborhood column
    """
    data['in_expensive_neighborhood'] = ...
    data['in_expensive_neighborhood'] = data['Neighborhood Code'].isin(neighborhoods).astype('int32') # SOLUTION NO PROMPT
    return data

def substitute_roof_material(data):
    """
    Input:
      data (data frame): a data frame containing a 'Roof Material' column.  Its values
                         should be limited to those found in the codebook
    Output:
      data frame identical to the input except with a refactored 'Roof Material' column
    """
    replacements = {
        'Roof Material': {
            1: 'Shingle/Asphalt',
            2: 'Tar&Gravel',
            3: 'Slate',
            4: 'Shake',
            5: 'Tile',
            6: 'Other',
        }
    }

    data = data.replace(replacements)
    return data

from sklearn.preprocessing import OneHotEncoder

def ohe_roof_material(data):
    """
    One-hot-encodes roof material.  New columns are of the form x0_MATERIAL.
    """
    ...
    # BEGIN SOLUTION NO PROMPT
    oh_enc = OneHotEncoder()
    oh_enc.fit(data[['Roof Material']])
    dummies = pd.DataFrame(oh_enc.transform(data[['Roof Material']]).todense(),
                           columns=oh_enc.get_feature_names(),
                           index = data.index)
    return data.join(dummies)
    # END SOLUTION
