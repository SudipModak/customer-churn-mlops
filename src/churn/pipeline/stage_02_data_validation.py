from src.churn.configuration.configuration import ConfigurationManager
from src.churn.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()

        vaidation_config = (config.get_data_validation_config())
        validation = DataValidation(
            config = vaidation_config
        )

        validation.validate_all_columns()