test = {   'name': 'q6c',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> assert len(simulations) == 100000\n'
                                               '>>> assert sum([-1 < x < 1 for x in simulations]) == len(simulations)\n'
                                               '>>> assert abs(np.mean(simulations) - 0.007) <= 0.016\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
