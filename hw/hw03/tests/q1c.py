test = {   'name': 'q1c',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> assert set(tweets.keys()) == {"AOC", "Cristiano", "elonmusk"}\n>>> assert all(df.index.name == "id" for df in tweets.values())\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> expected_cols = ['created_at', 'id_str', 'full_text', 'truncated', 'display_text_range',\n"
                                               "...        'entities', 'source', 'in_reply_to_status_id',\n"
                                               "...        'in_reply_to_status_id_str', 'in_reply_to_user_id',\n"
                                               "...        'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'user', 'geo',\n"
                                               "...        'coordinates', 'place', 'contributors', 'retweeted_status',\n"
                                               "...        'is_quote_status', 'retweet_count', 'favorite_count', 'favorited',\n"
                                               "...        'retweeted', 'lang', 'possibly_sensitive', 'extended_entities',\n"
                                               "...        'quoted_status_id', 'quoted_status_id_str', 'quoted_status_permalink',\n"
                                               "...        'quoted_status']\n"
                                               '>>> all(col in df.columns for df in tweets.values() for col in expected_cols)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> (tweets["AOC"].shape[0] is not None) and (tweets["AOC"].shape[0] >= 30)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> (tweets["Cristiano"].shape[0] is not None) and (tweets["Cristiano"].shape[0] >= 30)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> (tweets["elonmusk"].shape[0] is not None) and (tweets["elonmusk"].shape[0] >= 30)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.random.seed(42)\n'
                                               '>>> exp = set([1333958991613923331,\n'
                                               '...  1312936075590074368,\n'
                                               '...  1248798917350883337,\n'
                                               '...  1204575943601328128,\n'
                                               '...  1346163629486387201,\n'
                                               '...  1246500923180036096,\n'
                                               '...  1315825309036564482,\n'
                                               '...  1255121845533229056,\n'
                                               '...  1352691282603364362,\n'
                                               '...  1243377508835381249])\n'
                                               '>>> set(np.random.choice(sorted(tweets["AOC"].index), replace=False, size=10)) == exp\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.random.seed(42)\n'
                                               '>>> exp = set([880473340619759616,\n'
                                               '...  174892632500219905,\n'
                                               '...  284705925351239680,\n'
                                               '...  403528698936041473,\n'
                                               '...  476770924587667456,\n'
                                               '...  697801434755133440,\n'
                                               '...  1214232898917801984,\n'
                                               '...  741648660476383233,\n'
                                               '...  48000397721337856,\n'
                                               '...  95524319232409600])\n'
                                               '>>> set(np.random.choice(sorted(tweets["Cristiano"].index), replace=False, size=10)) == exp\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.random.seed(42)\n'
                                               '>>> exp = set([1265750340613427200,\n'
                                               '...  1321275062998257665,\n'
                                               '...  1285430635088076800,\n'
                                               '...  1252987963329388544,\n'
                                               '...  1339567835840962560,\n'
                                               '...  1313512170336944128,\n'
                                               '...  1348823685445136385,\n'
                                               '...  1280090680430178305,\n'
                                               '...  1301647642846547971,\n'
                                               '...  1281695247626416129])\n'
                                               '>>> set(np.random.choice(sorted(tweets["elonmusk"].index), replace=False, size=10)) == exp\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
