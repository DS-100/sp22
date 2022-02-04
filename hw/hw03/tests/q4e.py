test = {   'name': 'q4e',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> assert all(not isinstance(df.index, pd.MultiIndex) for df in mentions.values())\n'
                                               '>>> assert all(set(df.columns) == {"mentions"} for df in mentions.values())\n'
                                               '>>> assert set(mentions.keys()) == {"AOC", "Cristiano", "elonmusk"}\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> horiz_mentions = horiz_concat_df(mentions)\n>>> horiz_mentions.loc[0]["AOC"]["mentions"] == \'repescobar\'\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> horiz_mentions = horiz_concat_df(mentions)\n'
                                               ">>> list(sorted(horiz_mentions.columns)) == [('AOC', 'mentions'), ('Cristiano', 'mentions'), ('elonmusk', 'mentions')]\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
