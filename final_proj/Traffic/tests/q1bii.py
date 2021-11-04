test = {   'name': 'q1bii',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> not speeds_to_gps.isnull().any().any() # test if you correctly only include node with mapping\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> _mask = ((speeds_to_gps['osm_start_node_id'] == 26118026) * (speeds_to_gps['osm_end_node_id'] == 259458979) * (speeds_to_gps['day'] == 1))\n"
                                               '>>> _row = speeds_to_gps[_mask]\n'
                                               ">>> lat, lon = _row[['Latitude', 'Longitude']].values[0]\n"
                                               '>>> (lat == 37.6752805) and (lon == -122.3891936) # test if you correctly mapped nodes to GPS coords\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> len(speeds_to_gps) == 417639\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
