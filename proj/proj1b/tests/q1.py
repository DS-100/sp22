test = {   'name': 'q1',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> train.shape == (163833, 62) # train should contain 80% of the data\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> test.shape == (40959, 62) # test should contain 20% of the data\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.isclose(train["Sale Price"].mean(), 244939.22668204817, atol=0.1) # If this doesn\'t match, you might have still answered the question, but '
                                               'please adjust your code so that your split matches ours by following the implementation instructions about using shuffled_indices to split the data.\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(test["Sale Price"].mean(), 246066.1821089382, atol=0.1) # If this doesn\'t match, you might have still answered the question, but '
                                               'please adjust your code so that your split matches ours by following the implementation instructions about using shuffled_indices to split the data.\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
