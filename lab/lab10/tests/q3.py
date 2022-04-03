test = {   'name': 'q3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> res_q3.shape == (10, 3)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> set(res_q3.columns) == set(['title', 'numVotes', 'averageRating'])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.sum(res_q3['numVotes'].astype(int)) == 19870486\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> list(res_q3['title']) == ['The Shawshank Redemption',\n"
                                               "...  'The Dark Knight',\n"
                                               "...  'Inception',\n"
                                               "...  'Fight Club',\n"
                                               "...  'Pulp Fiction',\n"
                                               "...  'Forrest Gump',\n"
                                               "...  'Game of Thrones',\n"
                                               "...  'The Matrix',\n"
                                               "...  'The Lord of the Rings: The Fellowship of the Ring',\n"
                                               "...  'The Lord of the Rings: The Return of the King']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
