import pandas as pd
import numpy as np
import json

data = pd.read_csv('data/model_data/test_data.csv')
data.drop('Unnamed: 0', axis=1, inplace=True)
# data.to_csv('data/model_data/test_data.csv')
# model_data = pd.read_parquet('data/model_data/model_data.parquet')
# model_data.drop('churn_label', axis=1, inplace=True)
# # print(data.columns.tolist())
# # # print(data.head(3))
# print(model_data.columns.tolist())
# # print(model_data.head(3))


class TestData():
    def __init__(self, df:pd.DataFrame):
        self.df = df

    def check(self):
        model_data = pd.read_parquet('data/model_data/model_data.parquet')
        model_data.drop('churn_label', axis=1, inplace=True)

        if model_data.columns.tolist() != self.df.columns.tolist():
            raise ValueError('--- not a valid test data\n data is not according to trained model')
        else:
            print('+++ data validated')


obj = TestData(data)
obj.check()