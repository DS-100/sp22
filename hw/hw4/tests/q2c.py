test = {   'name': 'q2c',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> set(tweets.keys()) == {"AOC", "Cristiano", \'elonmusk\'}\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all("device" in df.columns for df in tweets.values())\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> counts = tweets["AOC"]["device"].value_counts().to_dict()\n'
                                               ">>> (set(counts.keys()) == {'Twitter Media Studio', 'Twitter for iPhone'}) and (set(counts.values()) == {2, 3245})\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.random.seed(10202)\n'
                                               ">>> expected = ['Twitter for iPhone'] * 10\n"
                                               '>>> actual = []\n'
                                               '>>> for i in np.random.choice(sorted(tweets["AOC"].index), replace=False, size=10):\n'
                                               '...     actual.append(tweets["AOC"].loc[i, "device"])\n'
                                               '>>> actual == expected\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
