from dataclasses import dataclass
from pathlib import Path



@dataclass
class DataIngestionArtifact:
    raw_data_path: Path

@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_data_path: Path

@dataclass
class DataTransformationArtifact:
    transformed_train_path: Path
    transformed_test_path: Path
    preprocessor_path: Path

@dataclass
class ModelTrainerArtifact:
    trained_model_path: Path
    train_accuracy: float
    test_accuracy: float
    f1_score: float

@dataclass 
class ModelEvaluationArtifact:
    run_id: str