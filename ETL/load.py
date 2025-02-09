"""
    Add AWS credentials in cli before running this file
    !pip install awscli
    !aws configure...
"""

import boto3

bucket_name = 'aws-s3-data-for-projects'

file1 = 'data/clean_data/clean_data.parquet'
s3_path1 = 'data/clean_data/clean_data.parquet'

file2 = 'data/model_data/model_data.parquet'
s3_path2 = 'data/model_data/model_data.parquet'

file3 = 'notebook/note.txt'
s3_path3 = 'data/note.txt'

s3 = boto3.client('s3')
s3.upload_file(file1, bucket_name, s3_path1)
s3.upload_file(file2, bucket_name, s3_path2)
s3.upload_file(file3, bucket_name, s3_path3)

print('Complete')

# ## pip install s3fs

# ## TO READ DATA
# import pandas as pd

# bucket_name = 'aws-customer-churn-bucket'
# s3_path = 'data/customer_info.csv'
# s3_url = f's3://{bucket_name}/{s3_path}'

# # Read the file directly using pandas and s3fs
# data = pd.read_csv(s3_url)

# # Now you can work with your DataFrame
# print(data.head())