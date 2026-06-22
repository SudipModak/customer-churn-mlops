from pathlib import Path

from src.churn.configuration.configuration import ConfigurationManager
from src.churn.components.data_transformation import DataTransformation
from src.churn.entity.artifact_entity import DataValidationArtifact


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()

        transformation_config = (
            config.get_data_transformation_config()
        )

        validation_artifact = DataValidationArtifact(
            validation_status=True,
            valid_data_path=Path("dummy")
        )

        transformation = DataTransformation(
            data_transformation_config=transformation_config,
            data_validation_artifact=validation_artifact
        )

        transformation_artifact = (
            transformation.initiate_data_transformation()
        )

        return transformation_artifact