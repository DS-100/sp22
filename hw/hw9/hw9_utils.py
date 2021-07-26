import sys
import numpy as np

try:
    import plotly
    import plotly.graph_objs as go
except ImportError:
    print(
        "Plotly Package not found. Please run: pip install plotly",
        file=sys.stderr)


def plot_3d(theta_1_series, theta_2_series, loss_series, loss_function, model, x, y):
    """Plot 3D Surface and trace of gradient. 
        
    The function takes the following as argument:
        theta_1: a list or array of theta_1 value
        theta_2: a list or array of theta_2 value
        loss: a list or array of loss value
        loss_function: for example, l2_loss
        model: for example, sin_model
        x: the original x input
        y: the original y output
    """
    plotly.offline.init_notebook_mode(connected=True)

    # Create trace of gradient
    trace = go.Scatter3d(
        x=theta_1_series,
        y=theta_2_series,
        z=loss_series,
        marker=dict(
            size=4,
            color=-loss_series,
            colorscale='Viridis',
        ),
        line=dict(color='rgb(50,170, 140)', width=3))

    # Create loss surface
    t1_s = np.linspace(np.min(theta_1_series) - 0.1, np.max(theta_1_series) + 0.1)
    t2_s = np.linspace(np.min(theta_2_series) - 0.1, np.max(theta_2_series) + 0.1)

    x_s, y_s = np.meshgrid(t1_s, t2_s)
    data = np.stack([x_s.flatten(), y_s.flatten()]).T
    ls = []
    for t1, t2 in data:
        l = loss_function(model(x, np.array([t1, t2])), y)
        ls.append(l)
    z = np.array(ls).reshape(50, 50)

    surface = go.Surface(x=t1_s, y=t2_s, z=z)

    # Our plot will be overlay of trace and surface
    data = [trace, surface]

    layout = dict(
        width=800,
        height=700,
        autosize=True,
        title='Gradient Descent',
        scene=dict(
            xaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
            ),
            yaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
            ),
            zaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
            ),
            camera=dict(
                up=dict(x=0, y=0, z=1),
                eye=dict(
                    x=-1.7428,
                    y=1.0707,
                    z=0.7100,
                )),
            aspectratio=dict(x=1, y=1, z=0.7),
            aspectmode='manual'),
    )

    fig = dict(data=data, layout=layout)

    plotly.offline.iplot(fig)
