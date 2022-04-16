test = {   'name': 'q1a',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> lr_model(np.arange(-2,2), np.arange(1,5)) == 0.5\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> (lr_model(2*np.eye(100), np.ones(100)) == sigmoid(2)*np.ones(100)).all()\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> test_theta = np.array([-3, 2, -1])\n'
                                               '>>> test_x = np.array([[1, 3, 5], [2, 4, 6]])\n'
                                               '>>> expected = np.array([0.11920292, 0.01798621])\n'
                                               '>>> actual = lr_model(test_theta, test_x)\n'
                                               '>>> np.isclose(actual, expected).all()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
