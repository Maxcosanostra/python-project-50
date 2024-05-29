import json
import yaml
import os


def read_file(file_path):
    if not os.path.isabs(file_path):
        file_path = os.path.join(
            os.path.dirname(__file__), '../tests/fixtures', file_path
        )
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
            return yaml.safe_load(file)
        else:
            raise ValueError("Unsupported file format")
