from pathlib import Path


from churn.utils.common import read_yaml
from churn.entity.config_entity import(
    DataIngestionConfig,
    DataValidationConfig
)

class ConfigurationManager:

    def __init__(self,
                 config_filepath=Path("configs/config.yaml")):
        
        self.config=read_yaml(config_filepath)

    def get_data_ingestion_config(self):

        config=self.config["data_ingestion"]

        return DataIngestionConfig(
            root_dir=Path(config["root_dir"]),
            raw_data_path=Path(config["raw_data_path"])
        )
    
    def get_data_validation_config(self):
        config=self.config["data_validation"]

        return DataValidationConfig(
            root_dir=Path(config["root_dir"]),
            status_file=Path(config["status_file"])
        )