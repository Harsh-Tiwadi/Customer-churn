import mysql.connector
import pandas as pd
from pathlib import Path


class ExtractDataSql():
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def get_data(self, query)->pd.DataFrame:
        try:
            conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
            print(f"+++ Connecting to database {self.database} on {self.host} with user {self.user}")

            if conn.is_connected():
                print("+++ Connection established.")
                # get data
                cursor = conn.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                df = pd.DataFrame(rows, columns=columns)
                # close connection
                cursor.close()
                conn.close()
            else:
                raise Exception("--- Failed to connect to the database.")
            return df

        except Exception as e:
            print(f"--- Error occurred: {e}")

class ExtractData():
    def get_data(self, file_path:str, dir=False):
        try:
            if dir==False and file_path[-4:]=='.csv':
                data = pd.read_csv(file_path)
                return data
            elif dir==True:
                dir_path =Path(file_path)
                csv_files = list(dir_path.glob('*.csv'))
                return {csv_file.stem:pd.read_csv(csv_file) for csv_file in csv_files}
        except Exception as e:
            print(e)

