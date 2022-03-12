test = {   'name': 'q4',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> training_data.shape[0] # Make sure that two observations were removed\n168931', 'hidden': False, 'locked': False},
                                   {   'code': ">>> # Make sure that remove_outliers doesn't mutate its input\n"
                                               ">>> remove_outliers(training_data, 'Building Square Feet', upper=2000).shape != training_data.shape\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
