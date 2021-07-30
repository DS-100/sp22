import scipy.io
import numpy as np
import pandas as pd

def load():
    mnist = scipy.io.loadmat('mnist_data.mat')
    X_train = mnist['training_data']
    y_train = mnist['training_labels'].reshape(X_train.shape[0])
    X_test = mnist['test_data']
    return X_train, y_train, X_test

def standardize(X_train, X_test):
    col_means = np.mean(X_train, axis = 0)
    col_sds = np.std(X_train, axis = 0)
    col_sds[col_sds == 0] = 1
    X_train = (X_train - col_means) / col_sds
    X_test = (X_test - col_means) / col_sds
    return X_train, X_test

def results_to_csv(y_test, file):
    y_test = y_test.astype(int)
    df = pd.DataFrame({'Category': y_test})
    df.index = df.index + 1  # Ensures that the index starts at 1.
    df.to_csv(file, index_label = 'Id')