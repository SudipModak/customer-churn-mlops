from pathlib import Path
from churn.utils.common import read_yaml

class ConfigurationManager:

    def __init__(self,
                 config_filepath=Path("configs/config.yaml")):
        
        self.config=read_yaml(config_filepath)

    def get_data_ingestion_config(self):
        return self.config["data_ingestion"]
    
    def get_data_validation_config(self):
        return self.config["data_validation"]