from mysql.connector import connect

from churn.logger.logger import logging
from churn.exception.exception import CustomException
import sys

def get_mysql_connection(
        host:str,
        user:str,
        password:str,
        database:str
):
    try:
        conn = connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        logging.info("Mysql Connection Established")

        return conn

    except Exception as e:
        raise CustomException(e, sys)