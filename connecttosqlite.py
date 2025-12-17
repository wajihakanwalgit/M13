from google.colab import files
import sqlite3
file=files.upload()
database= "database.sqlite"
conn= sqlite2.connect(database)
print("opened data sucessfully")
import pandas as pd
tables=pd.read_sql("select * from sqlite_master where type='table';""",conn)
tables