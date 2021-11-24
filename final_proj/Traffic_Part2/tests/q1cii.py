test = {   'name': 'q1cii',
    'points': 4,
    'suites': [   {   'cases': [   {'code': '>>> len(speeds_to_tract) == 418848\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> _mask = ((speeds_to_tract['osm_start_node_id'] == 5429620647) * (speeds_to_tract['osm_end_node_id'] == 65333834) * (speeds_to_tract['day'] == "
                                               '16))\n'
                                               '>>> _row = speeds_to_tract[_mask]\n'
                                               ">>> int(_row['MOVEMENT_ID']) == 9\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
