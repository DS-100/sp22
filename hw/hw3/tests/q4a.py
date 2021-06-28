test = {   'name': 'q4a',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> "name" in ins_named and "address" in ins_named\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> ins_named[ins_named["Missing Score"] == True].shape[0] == 0\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> ins_named.reset_index()['date'].equals(ins[ins['score'] > 0].reset_index()['date'])\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
