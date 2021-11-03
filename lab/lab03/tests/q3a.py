test = {   'name': 'q3a',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> import matplotlib \n>>> np.alltrue(np.array([l.get_text() for l in ax_4a.xaxis.get_ticklabels()]) == days)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import matplotlib \n'
                                               '>>> bars = [rect.get_height() for rect in ax_4a.get_children() \n'
                                               '...         if isinstance(rect, matplotlib.patches.Rectangle) and rect.get_x() != 0.0\n'
                                               '...        ]\n'
                                               '>>> \n'
                                               ">>> np.allclose(np.array(bars)[-7:], filtered['Day'].value_counts()[days].values)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> plt.close('all')\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
