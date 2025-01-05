import boto3

bucket_name = 'aws-customer-churn-bucket'
file = 'data/customer churn/Customer_Info.csv'
s3_path = 'data/customer_info.csv'

s3 = boto3.client('s3')
s3.upload_file(file, bucket_name, s3_path)



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