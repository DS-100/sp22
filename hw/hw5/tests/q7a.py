test = {   'name': 'q7a',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> assert res_q7a.shape == (10, 3)\n>>> list(res_q7a.columns) == ['nconst1', 'nconst2', 'tconst']\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> res_q7a['nconst1'].sum() % 9884 + res_q7a['nconst2'].sum() % 1234 + res_q7a['tconst'].sum() % 2223 == 11564\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
