test = {   'name': 'q3a',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> all("hour" in df.columns for df in tweets.values())\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(0 <= df["hour"].min() and 24 >= df["hour"].max() for df in tweets.values())\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
