test = {   'name': 'q1c',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> np.isclose(we_pos3_age_30, 1.521489768014793)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.isclose(weighted_metric(nba_data.loc[nba_data['Age'] >= 35, 'Pos3'], nba_data.loc[nba_data['Age'] < 35, 'Pos3'], entropy), 1.5163491026514833)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.isclose(weighted_metric(nba_data.loc[nba_data['Age'] >= 25, 'Pos3'], nba_data.loc[nba_data['Age'] < 25, 'Pos3'], gini_impurity), "
                                               '0.6295615251742243)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.isclose(weighted_metric(nba_data.loc[nba_data['Age'] >= 25, 'PTS'], nba_data.loc[nba_data['Age'] < 25, 'PTS'], variance), 21.01837881314829)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
