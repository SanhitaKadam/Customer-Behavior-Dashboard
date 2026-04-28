import pandas as pd
import mysql.connector

# load cleaned data
df = pd.read_csv("clean_data.csv")

# connect MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prathamesh@1234",
    database="sales_dashboard"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    sql = """INSERT INTO sales_data
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    cursor.execute(sql, tuple(row))

conn.commit()
print("Data Inserted Successfully!")
print("Done")
