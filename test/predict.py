import pandas as pd
import numpy as np
import json
import joblib

from test_data import TestData

# data
data = pd.read_csv('data/model_data/test_data.csv')

def predict_test_data(df:pd.DataFrame):

