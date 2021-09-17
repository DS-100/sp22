test = {   'name': 'q3c',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> all("converted_time" in df.columns for df in tweets.values())\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all((df["converted_time"] == df["created_at"]).all() for df in tweets.values())\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(df["converted_time"].dt.tz != df["created_at"].dt.tz for df in tweets.values())\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
