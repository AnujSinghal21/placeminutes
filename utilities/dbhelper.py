import sqlite3
import pandas as pd
DB_PATH = '../data.db'
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

df=pd.DataFrame(cursor.execute("SELECT * FROM OPENINGS"))

df.to_csv('bakait.csv',index=False)