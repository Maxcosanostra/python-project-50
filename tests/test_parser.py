import pytest
from gendiff.parser import parse_data


@pytest.mark.parametrize("file_content, format, expected_output", [
    ('{"key": "value"}', 'json', {"key": "value"}),
    ("key: value", "yaml", {"key": "value"}),
])
def test_parse_data(file_content, format, expected_output):
    assert parse_data(file_content, format) == expected_output
