test = {   'name': 'q2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': ">>> np.allclose(words_in_texts(['hello', 'bye', 'world'], \n"
                                               "...                            pd.Series(['hello', 'hello worldhello'])),\n"
                                               '...             np.array([[1, 0, 0], \n'
                                               '...                       [1, 0, 1]]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.allclose(words_in_texts(['a', 'b', 'c', 'd', 'e', 'f', 'g'], \n"
                                               "...                            pd.Series(['a b c d ef g', 'a', 'b', 'c', 'd e f g', 'h', 'a h'])),\n"
                                               '...             np.array([[1,1,1,1,1,1,1], \n'
                                               '...                       [1,0,0,0,0,0,0],\n'
                                               '...                       [0,1,0,0,0,0,0],\n'
                                               '...                       [0,0,1,0,0,0,0],\n'
                                               '...                       [0,0,0,1,1,1,1],\n'
                                               '...                       [0,0,0,0,0,0,0],\n'
                                               '...                       [1,0,0,0,0,0,0]]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
