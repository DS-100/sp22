test = {   'name': 'q1e',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> county_data.shape == (3141, 639)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> not county_data.isna().to_numpy().any()\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> county_data['POPESTIMATE2020'].sum() == 329474777\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
