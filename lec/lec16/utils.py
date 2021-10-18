import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

def plot_y_vs_yhat(df, y, yhat):
    plt.figure()
    Y, Yhat = df[y], df[yhat]
    plt.scatter(Yhat, Y, label='(yhat, y)')
    cmin, cmax = max(Yhat.min(), Y.min()), min(Yhat.max(), Y.max())
    plt.plot([cmin, cmax], [cmin, cmax], color='red', label='y=yhat')
    plt.legend()
    
def plot_predictions(df, x, y, yhat):
    plt.figure()
    X, Y, Yhat = df[x], df[y], df[yhat]
    plt.plot(X, Y, label='ground truth')
    plt.plot(X, Yhat, label='prediction')
    plt.legend()
    
def plot_predictions_over_time(df, x, y, yhat):
    time = df.groupby(by='time').agg('mean').reset_index()
    plot_predictions(time, x, y, yhat)
    
def evaluate(df, y, yhat): 
    """Compute and print error metrics"""
    Y, Yhat = df[y], df[yhat]
    metrics = {
        'MSE': mean_squared_error(Y, Yhat),
        'MAE': mean_absolute_error(Y, Yhat),
        'RMSE': np.sqrt(mean_squared_error(Y, Yhat)),
    }
    print("Mean Squared Error:", metrics['MSE'])
    print("Mean Absolute Error:", metrics['MAE'])
    print("Root Mean Squared Error:", metrics['RMSE'])
    return metrics

def evaluate_and_plot(df, x, y, yhat):
    """Report error metrics and also visualize"""
    evaluate(df, y, yhat)
    plot_y_vs_yhat(df.sample(frac=0.01), y, yhat)
    plot_predictions_over_time(df, x, y, yhat)

def phi_curved(X):
    return np.hstack([
        X,
        X * X,
        np.expand_dims(np.prod(X, axis=1), 1),
        X ** 3,
    ])

def phi_periodic(X):
    return np.hstack([
        X,
        np.sin(X),
        np.sin(0.26*X),
        np.sin(X - 6),
        np.sin(0.26 * X - 6),
    ])

def phi_curved_and_periodic(X):
    return np.hstack([phi_curved(X), phi_periodic(X)])
