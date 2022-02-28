test = {   'name': 'q1b',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> linear_model(np.arange(1,5), np.arange(1,5)) == 30\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> (linear_model(2*np.eye(100), np.ones(100)) == 2*np.ones(100)).all()\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> test_theta = np.array([[1, 2], [3, 4], [5, 6]])\n'
                                               '>>> test_x = np.array([[1, 3, 5], [2, 4, 6]])\n'
                                               '>>> expected = np.array([[35, 44], [44, 56]])\n'
                                               '>>> actual = linear_model(test_theta, test_x)\n'
                                               '>>> np.array_equal(actual, expected)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
