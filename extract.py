import mysql.connector
import pandas as pd

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cat@968@",
    database="marketing"
)

# Create a cursor
cursor = conn.cursor()

# Execute a query
query = "SELECT * FROM marketing"
cursor.execute(query)

# Fetch data and convert to DataFrame
rows = cursor.fetchall()
columns = [col[0] for col in cursor.description]
df = pd.DataFrame(rows, columns=columns)

# Display the DataFrame
print(df.head())

# Close connections
cursor.close()
conn.close()
print(df.info())
print(df.isnull().sum())


def main():
