import pandas as pd
import yaml
import sys

from churn.entity.config_entity import DataValidationConfig
from churn.exception.exception import CustomException
from churn.logger.logger import logging


class DataValidation:

    def __init__(
        self,
        config: DataValidationConfig
    ):
        self.config = config

    def validate_all_columns(self):

        try:

            validation_status = True

            data = pd.read_excel(
                "artifacts/data_ingestion/raw.xlsx"
            )

            with open(
                "configs/schema.yaml",
                "r"
            ) as yaml_file:

                schema = yaml.safe_load(yaml_file)

            schema_cols = list(
                schema["COLUMNS"].keys()
            )

            data_cols = list(
                data.columns
            )

            if set(schema_cols) != set(data_cols):
                validation_status = False

            with open(
                self.config.status_file,
                "w"
            ) as f:

                f.write(
                    f"Validation Status: {validation_status}"
                )

            logging.info(
                f"Validation Status: {validation_status}"
            )

            return validation_status

        except Exception as e:
            raise CustomException(e, sys)