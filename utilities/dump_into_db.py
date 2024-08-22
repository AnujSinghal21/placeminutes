import sqlite3
import csv
import pandas

DB_PATH = "data/data.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# push_type -  in case the table exists : "fail" [Default], "replace", "append"
def csv_to_db(input_csv,table_name, push_type= "fail") :
    df = pandas.read_csv(input_csv)
    cursor.execute(f'SELECT name from sqlite_master where type = "table"')
    existing_tables = [ name  for i in cursor.fetchall() for name in i] 
    if(existing_tables.count(table_name) > 0 and push_type =="fail"):
        print(f"ERROR: Table {table_name} already exists")
        return None
    if(push_type == "replace"):
        print(f"WARNING: Replacing table {table_name}")
    df.to_sql(table_name,con=conn,if_exists=push_type)

csv_to_db("utilities/cleaned_data.csv","companies_csv", "replace")
csv_to_db("utilities/studentwise_stats.csv","students_csv", "replace")

cursor.
