import pandas as pd

class ExpModel():
    def __init__(self, df):
        self._df = df

    # Getter for the df attribute
    @property
    def df(self):
        if isinstance(self._df, pd.DataFrame):
            return self._df
        else:
            raise ValueError('Not a Dataframe')

    # Setter for the df attribute
    @df.setter
    def df(self, value):
        print('updating')
        if isinstance(value, list):
            self._df['name'] = value
        else:
            raise ValueError("Not a DataFrame.")

    def __str__(self):
        return f"{self.df}"

name = pd.DataFrame({'name':['jhon', 'james', 'jack'],'age':[34,23,35]})
model = ExpModel(name)
print(model)
model.df = (['harsh', 'k', 'l'])
print(model)