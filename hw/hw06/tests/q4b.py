test = {   'name': 'q4b',
    'points': 5,
    'suites': [   {   'cases': [   {'code': '>>> len(models) == 1000\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all([isinstance(model, lm.LinearRegression) for model in models])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all([len(model.coef_) == 5 and model.intercept_ != 0 for model in models])\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
