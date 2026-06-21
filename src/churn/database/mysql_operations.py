import pandas as pd
import sys
import json

from churn.database.mysql_connection import get_mysql_connection
from churn.exception.exception import CustomException


def read_table(
        host,
        user,
        password,
        database,
        query
):
    try:
        conn = get_mysql_connection(
            host=host,
            user=user,
            password=password,
            database=database
        )

        df = pd.read_sql(
            query,
            conn
        )

        conn.close()

        return df

    except Exception as e:
        raise CustomException(e, sys)


def save_upload_history(
        host,
        user,
        password,
        database,
        file_name,
        total_records
):
    try:
        conn = get_mysql_connection(
            host,
            user,
            password,
            database
        )

        cursor = conn.cursor()

        query = """
        INSERT INTO upload_history
        (file_name, total_records)
        VALUES (%s, %s)
        """

        cursor.execute(
            query,
            (
                file_name,
                total_records
            )
        )

        conn.commit()

        upload_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return upload_id

    except Exception as e:
        raise CustomException(e, sys)


def save_customer_uploads(
        host,
        user,
        password,
        database,
        upload_id,
        df
):
    try:
        conn = get_mysql_connection(
            host,
            user,
            password,
            database
        )

        cursor = conn.cursor()

        query = """
        INSERT INTO customer_uploads
        (upload_id, customer_id, raw_data)
        VALUES (%s, %s, %s)
        """

        for _, row in df.iterrows():

            customer_id = str(
                row.get(
                    "CustomerID",
                    "UNKNOWN"
                )
            )

            row_dict = {}

            for col, value in row.items():

                if pd.isna(value):
                    row_dict[col] = None
                else:
                    row_dict[col] = value

            raw_json = json.dumps(
                row_dict,
                default=str
            )

            cursor.execute(
                query,
                (
                    upload_id,
                    customer_id,
                    raw_json
                )
            )

        conn.commit()

        cursor.close()
        conn.close()

    except Exception as e:
        raise CustomException(e, sys)


def save_prediction_results(
        host,
        user,
        password,
        database,
        upload_id,
        customer_ids,
        predictions
):
    try:
        conn = get_mysql_connection(
            host,
            user,
            password,
            database
        )

        cursor = conn.cursor()

        query = """
        INSERT INTO prediction_results
        (upload_id, customer_id, prediction)
        VALUES (%s, %s, %s)
        """

        for customer_id, pred in zip(
                customer_ids,
                predictions
        ):

            cursor.execute(
                query,
                (
                    upload_id,
                    str(customer_id),
                    int(pred)
                )
            )

        conn.commit()

        cursor.close()
        conn.close()

    except Exception as e:
        raise CustomException(e, sys)