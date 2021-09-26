test = {   'name': 'q6b',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': ">>> assert res_q6b.shape == (10, 4)\n>>> list(res_q6b.columns) == ['numAList', 'numBList', 'numCList', 'primaryTitle']\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert set(res_q6b['primaryTitle']) == {'A Few Good Men',\n"
                                               "...  'Back to the Future',\n"
                                               "...  'Die Hard',\n"
                                               "...  'Forrest Gump',\n"
                                               "...  'Goodfellas',\n"
                                               "...  'Star Wars: Episode V - The Empire Strikes Back',\n"
                                               "...  'Terminator 2: Judgment Day',\n"
                                               "...  'The Godfather',\n"
                                               "...  'The Godfather: Part II',\n"
                                               "...  'The Silence of the Lambs'}\n"
                                               ">>> list(set(res_q6b['numAList']))[0] == 10\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> np.sum(res_q6a['isBList'] + res_q6a['isCList']) == 0\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
