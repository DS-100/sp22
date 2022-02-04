test = {   'name': 'q2c',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> import matplotlib \n'
                                               '>>> xy_data = ax_3d.lines[0].get_xydata()\n'
                                               '>>> expected_xy_data = np.vstack((hours, calls["Hour"].value_counts()[hours].to_numpy())).T\n'
                                               '>>> np.allclose(xy_data, expected_xy_data)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> plt.close('all')\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
