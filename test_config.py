from churn.configuration.configuration import ConfigurationManager

config=ConfigurationManager()
print(config.get_data_ingestion_config())
print(config.get_data_validation_config())