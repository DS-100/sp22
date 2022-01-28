test = {   'name': 'q2f',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> assert 'postal5' in bus.columns\n>>> (bus['postal5'].str.len() != 5).sum() == 221\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert bus['postal5'].isin(valid_zips).sum() == 6032\n>>> bus['postal5'].isna().sum() == 221\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
