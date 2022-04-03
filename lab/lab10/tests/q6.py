test = {   'name': 'q6',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> res_q6.shape == (10, 4)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> sorted(res_q6['total_amount']) == [1000, 2000, 2600, 5000, 5000, 5200, 5400, 9000, 10000, 18633157]\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> sorted(res_q6['num_donations']) == [1, 1, 1, 1, 1, 1, 1, 2, 2, 131]\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> sorted(res_q6['cmte_nm']) == [\n"
                                               "...     'DONALD J. TRUMP FOR PRESIDENT, INC.',\n"
                                               "...     'DONOVAN FOR CONGRESS',\n"
                                               "...     'FRIENDS OF DAVE BRAT INC.',\n"
                                               "...     'GRASSLEY COMMITTEE INC',\n"
                                               "...     'HELLER FOR SENATE',\n"
                                               "...     'NEW HAMPSHIRE REPUBLICAN STATE COMMITTEE',\n"
                                               "...     'NY REPUBLICAN FEDERAL CAMPAIGN COMMITTEE',\n"
                                               "...     'REPUBLICAN PARTY OF IOWA',\n"
                                               "...     'SOUTH CAROLINA REPUBLICAN PARTY',\n"
                                               "...     'TEXANS FOR SENATOR JOHN CORNYN INC']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
