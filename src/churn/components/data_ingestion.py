import pandas as pd
import openpyxl
from churn.entity.config_entity import DataIngestionConfig
from churn.logger.logger import logging
from churn.exception.exception import CustomException
import sys
class DataIngestion:
    def __init__(
            self,
            config: DataIngestionConfig
    ):
        self.config = config

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
            logging.info("Raw data saved successfully")

            return self.config.raw_data_path
        except Exception as e:
            raise CustomException(e, sys)