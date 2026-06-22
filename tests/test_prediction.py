import pandas as pd
from src.churn.ml.prediction import PredictionPipeline
from src.churn.database.mysql_connection import get_mysql_connection


conn= get_mysql_connection(
    host="localhost",
    user= "root",
    password ="Sudip@2003",
    database = "churn_db")


df=pd.read_sql(
    
    "SELECT * from customer_churn_raw",conn)
conn.close()

if "Churn Label" in df.columns:
    df = df.drop(columns=["Churn Label"])
pipeline = PredictionPipeline()

predictions= pipeline.predict(df.head(10))

pipeline = PredictionPipeline()

predictions = pipeline.predict(df.head(10))


print(predictions)