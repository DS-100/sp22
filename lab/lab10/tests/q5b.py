test = {   'name': 'q5b',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> res_q5b.shape == (5, 2)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> all(res_q5b == res_q5b.sort_values('cand_name', ascending=False))\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> sorted(map(str, res_q5b['cmte_nm'].unique())) == [\n"
                                               "...     'CITIZENS TO ELECT DANIEL P ZUTLER FOR PRESIDENT',\n"
                                               "...     'JOE ZUCCOLO FOR CONGRESS',\n"
                                               "...     'None',\n"
                                               "...     'ZUKOWSKI FOR CONGRESS',\n"
                                               "...     'ZUMWALT FOR CONGRESS']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
