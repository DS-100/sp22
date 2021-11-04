test = {   'name': 'q4i',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> set(county_to_missing_dates.keys()) == set(['Del Norte',\n"
                                               "...  'Trinity',\n"
                                               "...  'Lake',\n"
                                               "...  'Tuolumne',\n"
                                               "...  'Amador',\n"
                                               "...  'Plumas',\n"
                                               "...  'Calaveras',\n"
                                               "...  'Glenn',\n"
                                               "...  'Napa'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> county_to_missing_dates['Napa'][0] == '2020-11-04'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> '2020-08-03' in county_to_missing_dates['Trinity']\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
