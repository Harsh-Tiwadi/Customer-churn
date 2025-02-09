import pandas as pd
import numpy as np
import json

info = {}

def skip(skip_saved=True):
    # global skip_saved
    skip_saved = bool(int(input('Want to save the run ? True[1]/False[0]: ')))
    return skip_saved
skip_saved = skip()
print('skip_saved','-', skip_saved)

# to save info
def save_info(item:dict):
    if skip_saved:
        print('--- Skipped Info Saved')
    else:
        with open('EDA/EDA.json', 'w') as file:
            file.write(json.dumps(item))
        print('+++ Info Saved')

# to save the data
def save_data(data:pd.DataFrame, path:str):
    if skip_saved:
        print('--- Skipped Data Saved')
    else:
        data.to_parquet(path)
        print('+++ Data Saved')

# read all data
df1 = pd.read_csv("data/customer churn/Customer_Info.csv")
df2 = pd.read_csv("data/customer churn/Location_Data.csv")
df3 = pd.read_csv("data/customer churn/Online_Services.csv")
df4 = pd.read_csv("data/customer churn/Payment_Info.csv")
df5 = pd.read_csv("data/customer churn/Service_Options.csv")
df6 = pd.read_csv("data/customer churn/Status_Analysis.csv")

# Reset the index of each DataFrame
df1 = df1.reset_index(drop=True)
df2 = df2.reset_index(drop=True)
df3 = df3.reset_index(drop=True)
df4 = df4.reset_index(drop=True)
df5 = df5.reset_index(drop=True)
df6 = df6.reset_index(drop=True)

# merged all data as number or row same across all
merged_df = pd.concat([df1,df2,df3,df4,df5,df6], axis=1)

# remove duplicated col.
info.update({'duplicated columns':merged_df.loc[:,merged_df.columns.duplicated()].columns.tolist()})
merged_df = merged_df.loc[:, ~merged_df.columns.duplicated()]


# # Saving:
# save_info(info)
# save_data(merged_df, 'data/merged_data/merged_data.parquet')  -- Checkpoint
