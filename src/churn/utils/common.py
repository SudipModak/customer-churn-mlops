import yaml
from pathlib import Path

def read_yaml(path_to_yaml: Path):
    with open(path_to_yaml, "r") as yaml_file:
        content=yaml.safe_load(yaml_file)
    return content