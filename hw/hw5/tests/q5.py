test = {   'name': 'q5',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> assert res_q5.shape == (10, 3)\n>>> list(res_q5.columns) == ['nconst', 'name', 'numVotes']\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> res_q5['numVotes'].sum() == 140593640\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> res_q5['nconst'].sum() == 1136095\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
