test = {   'name': 'q4d',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> df = pd.DataFrame({"full_text": ["a clean tweet", "an UPPPERcAsE tweet", "a ! tweet!!with..(*UF)punctuation"]})\n'
                                               '>>> df = sanitize_texts(df)\n'
                                               '>>> df["clean_text"].tolist() == [\'a clean tweet\', \'an upppercase tweet\', \'a   tweet  with    uf punctuation\']\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> all("clean_text" in df.columns for df in tweets.values())\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
