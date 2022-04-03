test = {   'name': 'q5a',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> res_q5a.shape == (5, 2)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> all(res_q5a == res_q5a.sort_values('cand_name', ascending=False))\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> sorted(res_q5a['cmte_nm'].unique()) == [\n"
                                               "...     'CITIZENS TO ELECT DANIEL P ZUTLER FOR PRESIDENT',\n"
                                               "...      'CONSTITUTIONAL COMMITTEE',\n"
                                               "...      'JOE ZUCCOLO FOR CONGRESS',\n"
                                               "...      'ZUKOWSKI FOR CONGRESS',\n"
                                               "...      'ZUMWALT FOR CONGRESS']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
