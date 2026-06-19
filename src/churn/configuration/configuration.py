from pathlib import Path



from churn.utils.common import read_yaml,create_directories
from churn.entity.config_entity import(
    DataIngestionConfig,
    DataValidationConfig,
    ModelTrainerConfig
)
from churn.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    MySQLConfig
)
class ConfigurationManager:

    def __init__(self,
                 config_filepath=Path("configs/config.yaml")):
        
        self.config=read_yaml(config_filepath)

    def get_data_ingestion_config(self):

        config=self.config["data_ingestion"]
        create_directories([config["root_dir"]])

        return DataIngestionConfig(
            root_dir=Path(config["root_dir"]),
            raw_data_path=Path(config["raw_data_path"])
        )
    
    def get_data_validation_config(self):
        config=self.config["data_validation"]

        create_directories([config["root_dir"]])

        return DataValidationConfig(
            root_dir=Path(config["root_dir"]),
            status_file=Path(config["status_file"])
        )
    
    def get_data_transformation_config(self):

        config = self.config["data_transformation"]

        create_directories([config["root_dir"]])

        return DataTransformationConfig(
            root_dir=Path(config["root_dir"]),
            transformed_train_path=Path(config["transformed_train_path"]),
            transformed_test_path=Path(config["transformed_test_path"]),
            preprocessor_path=Path(config["preprocessor_path"])
        )
    
    def get_mysql_config(self):
        config=self.config["mysql"]

        return MySQLConfig(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:

        config = self.config["model_trainer"]

        create_directories([config["root_dir"]])

        return ModelTrainerConfig(
            root_dir=Path(config["root_dir"]),
            trained_model_path=Path(config["trained_model_path"])
        )