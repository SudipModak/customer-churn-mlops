from churn.database.mysql_connection import get_mysql_connection

conn = get_mysql_connection(
    host="localhost",
    user="root",
    password="Sudip@2003",
    database="churn_db"
)

print("Connected Successfully")
conn.close()