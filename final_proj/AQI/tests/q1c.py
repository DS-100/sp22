test = {   'name': 'q1c',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': ">>> set(epa_data_CA_merged.columns) == set(['State Name', 'county Name', 'Month', 'Day', 'AQI', 'Category',\n"
                                               "...        'Defining Site', 'Latitude', 'Longitude'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert epa_data_CA_merged[epa_data_CA_merged['county Name'] == 'Alameda'].shape == (366, 9)\n"
                                               ">>> round(epa_data_CA_merged[(epa_data_CA_merged['county Name'] == 'Alameda') & (epa_data_CA_merged['Month'] == 1)\n"
                                               "...                   & (epa_data_CA_merged['Day'] == 1)]['Latitude'][0], 2) == 37.74\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
