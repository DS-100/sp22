test = {   'name': 'q6a',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> assert res_q6a.shape == (10, 4)\n>>> list(res_q6a.columns) == ['isAList', 'isBList', 'isCList', 'nconst']\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.sum(res_q6a['nconst'] * res_q6a['isAList'] + res_q6a['isBList'] + res_q6a['isCList']) == 1136095\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
