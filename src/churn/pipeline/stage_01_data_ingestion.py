from churn.configuration.configuration import ConfigurationManager
from churn.components.data_ingestion import DataIngestion


class DataIngestionTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()

        mysql_config = config.get_mysql_config()

        data_ingestion = DataIngestion(
            config=data_ingestion_config,
            mysql_config=mysql_config
        )

        data_ingestion.initiate_data_ingestion()