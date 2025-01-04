from extract import ExtractDataSql
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

# Validate configuration
if not all([host, user, password, database]):
    raise ValueError("One or more environment variables (host, user, password, database) are not set.")
else:
    print("DB config loaded successfully from .env")

extractor = ExtractDataSql(host, user, password, database)
data = extractor.get_data("select * from marketing")
print(data.head())