from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    raw_data_path: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    transformed_train_path: Path
    transformed_test_path: Path
    preprocessor_path: Path