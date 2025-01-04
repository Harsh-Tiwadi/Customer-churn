import mysql.connector
import pandas as pd


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
            print(f"Connecting to database {self.database} on {self.host} with user {self.user}")

            if conn.is_connected():
                print("Connection established.")
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
                raise Exception("Failed to connect to the database.")
            return df

        except Exception as e:
            print(f"Error occurred: {e}")
