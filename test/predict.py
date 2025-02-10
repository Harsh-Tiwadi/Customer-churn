import pandas as pd
import numpy as np
import json
import joblib

from test_data import TestData

# data
data = pd.read_csv('data/model_data/test_data.csv')

def predict_test_data(df:pd.DataFrame):
    obj = TestData(df)
    obj.check()
    model = joblib.load('model/saved_svm_model.joblib')
    y_pred = model.predict(df)
    df['pred'] = y_pred
    print("+++ Added prediction to test_data")
    return df

prediction = predict_test_data(data)

if int(input('type 1 for saving prediction')) == 1:
    prediction.to_csv('data/prediction/prediction.csv')
else:
    print('+++ skipped saving predictions')
