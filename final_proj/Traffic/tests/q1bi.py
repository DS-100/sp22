test = {   'name': 'q1bi',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> node_to_gps.shape == (19144, 3)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> mask_26118026 = node_to_gps['osm_node_id'] == 26118026\n"
                                               '>>> _, lat, lon = node_to_gps[mask_26118026].values[0]\n'
                                               '>>> (lat == 37.6752805) and (lon == -122.3891936)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
