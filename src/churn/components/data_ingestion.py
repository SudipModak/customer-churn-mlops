
import pandas as pd
import openpyxl
from src.churn.entity.config_entity import DataIngestionConfig
from src.churn.logger.logger import logging
from src.churn.exception.exception import CustomException
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import sys
class DataIngestion:
    def __init__(
            self,
            config: DataIngestionConfig,
            mysql_config
    ):
        self.config = config
        self.mysql_config=mysql_config

    def initiate_data_ingestion(self):
        try:
            logging.info(
                "Data Ingestion Started"
            )
            df= pd.read_excel("data/Telco_customer_churn.xlsx")
            df.to_excel(
                self.config.raw_data_path,
                index=False
            )
            password=quote_plus(self.mysql_config.password)
            engine= create_engine(
                f"mysql+pymysql://{self.mysql_config.user}:"
                f"{password}@"
                f"{self.mysql_config.host}:3306/"
                f"{self.mysql_config.database}"
            )

            df.to_sql(
                name="customer_churn_raw",
                con=engine,
                if_exists="replace",
                index=False
            )
            logging.info("raw data saved successfully")
            logging.info("Raw data loaded into MySql successfully")

            return self.config.raw_data_path
        except Exception as e:
            raise CustomException(e, sys)