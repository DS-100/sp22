test = {   'name': 'q3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> res_q3.shape == (5, 2)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> all(res_q3 == res_q3.sort_values('cand_name', ascending = False))\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> sorted(map(str, res_q3['cmte_nm'].unique())) == ['CITIZENS TO ELECT DANIEL P ZUTLER FOR PRESIDENT', 'JOE ZUCCOLO FOR CONGRESS', 'None', 'ZUKOWSKI "
                                               "FOR CONGRESS', 'ZUMWALT FOR CONGRESS']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
