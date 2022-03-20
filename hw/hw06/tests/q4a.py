test = {   'name': 'q4a',
    'points': 5,
    'suites': [   {   'cases': [   {'code': '>>> all([len(df_i) == len(mask_data) for df_i in bootstrap_sample(mask_data, 1)])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(bootstrap_sample(mask_data, 3)) == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(bootstrap_sample(mask_data, 1)[0]['NEVER'].mean(), 0.0799, atol = 8e-3)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
