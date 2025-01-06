from extract import ExtractData
from extract import ExtractDataSql #
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

# Validate configuration
if not all([host, user, password, database]):
    raise ValueError("--- One or more environment variables (host, user, password, database) are not set.")
else:
    print("+++ DB config loaded successfully from .env")

def save_data_for_notebook():
    try:
        extractor = ExtractDataSql(host, user, password, database) #
        data = extractor.get_data("select * from marketing")
        print("+++ Extracted the queried data")
    except Exception as e:
        print(f"--- Error while extracting {e}")
    if not data.empty and isinstance(data, pd.DataFrame):
        print('+++ got data')
    else:
        raise TypeError("--- Didn't got data")

    #print(data.shape)
    data.to_csv('data/notebook_data.csv', index=False)


def transform_data():
    extractor = ExtractData()
    data_dict = extractor.get_data('data/customer churn', dir=True)
    data = pd.concat(data_dict.values(), axis=1)
    data = data.loc[:, ~data.columns.duplicated()]
    return data

def save_data(data, verify:bool):
    if verify:
        data.to_csv('data/customer churn/merged_data.csv')
        print('+++ Merged data added successfully')
    else:
        print('please verify the data')




if __name__ == '__main__':
    data = transform_data()
    save_data(data, verify=True)