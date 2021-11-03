test = {   'name': 'q6a',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> assert len(draw_state_sample(1500, "florida")) == 3\n>>> assert sum(draw_state_sample(1500, "michigan")) == 1500\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> q7a_penn = draw_state_sample(1500, "pennsylvania")\n'
                                               '>>> trump_win_penn = (q7a_penn[0] - q7a_penn[1]) / 1500\n'
                                               '>>> abs(trump_win_penn - 0.007) <= 0.12\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
