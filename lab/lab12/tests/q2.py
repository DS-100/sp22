test = {   'name': 'q2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> len(lr_predict(theta_hat, X_intercept_train)) == len(Y_train)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.equal(lr_predict(np.array([2, 3, 0]),\n'
                                               '...                     np.array([[1, 0, -1], [-1, 0, 1]])),\n'
                                               '...          [1, 0])\n'
                                               'array([ True,  True])',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> np.sum(Y_train_pred == 1) == 139\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
