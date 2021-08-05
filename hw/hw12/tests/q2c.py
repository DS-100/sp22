test = {   'name': 'q2c',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(mid1_grades_centered_scaled, pd.DataFrame)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(np.isclose(np.mean(mid1_grades_centered_scaled), [0] * mid1_grades.shape[1]))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(np.isclose(np.var(mid1_grades_centered_scaled), [1] * mid1_grades.shape[1]))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
