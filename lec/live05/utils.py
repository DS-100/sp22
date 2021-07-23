from sklearn.metrics import mean_squared_error
import numpy as np

def rmse(y_true, y_pred):
    return mean_squared_error(y_true, y_pred, squared=False)


from sklearn.model_selection import KFold

def evaluate_models(models, data, feature_func):
    """
    Params:
    - model_types: dict of instantiated sklearn models (not fit yet)
    - data: training dataframe
    - feature_func: pipeline function transforming data into design matrix
    
    Returns:
    - prints average CV RMSE for each model
    """
    X, y = feature_func(data), data['popularity']
    kf = KFold(n_splits=5, shuffle=True, random_state=24)
    # For each model, compute the average validation RMSE
    for model in models.keys():
        train_rmses = []
        val_rmses = []
        # Perform CV
        for train_idx, val_idx in kf.split(X):
            X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
            X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]
            models[model].fit(X_train, y_train)
            
            # Compute train RMSE
            train_preds = models[model].predict(X_train)
            train_preds = np.clip(train_preds, a_min=0, a_max=100)    # 0 <= popularity <= 100
            train_preds = np.rint(train_preds)    # round to nearest integer
            train_rmses.append(rmse(y_train, train_preds))
            
            # Compute val RMSE
            val_preds = models[model].predict(X_val)
            val_preds = np.clip(val_preds, a_min=0, a_max=100)    # 0 <= popularity <= 100
            val_preds = np.rint(val_preds)    # round to nearest integer
            val_rmses.append(rmse(y_val, val_preds))
        print(f"{model} CV Train RMSE: {np.mean(train_rmses)}\t\t{model} CV Val RMSE: {np.mean(val_rmses)}")