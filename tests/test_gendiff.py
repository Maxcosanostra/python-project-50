import os
import pytest
from gendiff import generate_diff


def get_fixtures_path(file_name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', file_name)


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()


@pytest.mark.parametrize("file1, file2, expected_file, formatter", [
    ("file1.json", "file2.json", "expected_diff.txt", "stylish"),
    ("file1.yml", "file2.yml", "expected_diff.txt", "stylish"),
    ("flat_file1.json", "flat_file2.json", "expected_flat_diff.txt", "stylish"),
    ("flat_file1.yml", "flat_file2.yml", "expected_flat_diff.txt", "stylish"),
    ("file1.json", "file2.json", "expected_json_output.txt", "json"),
    ("file1.yml", "file2.yml", "expected_json_output.txt", "json"),
    ("file1.json", "file2.json", "expected_plain_output.txt", "plain"),
    ("file1.yml", "file2.yml", "expected_plain_output.txt", "plain")
])
def test_generate_diff(file1, file2, expected_file, formatter):
    file1_path = get_fixtures_path(file1)
    file2_path = get_fixtures_path(file2)
    expected_result = read_file(get_fixtures_path(expected_file))
    result = generate_diff(file1_path, file2_path, formatter)
    assert result == expected_result, (
        f"Failed on {formatter} with {file1} and {file2}"
    )
