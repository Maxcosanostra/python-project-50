import pytest
from gendiff.diff_gen import generate_diff


@pytest.fixture
def file1_path():
    return 'gendiff/files/file1.json'


@pytest.fixture
def file2_path():
    return 'gendiff/files/file2.json'


def test_generate_diff(file1_path, file2_path):
    expected_diff = (
        '- follow: False\n'
        '  proxy: 123.234.53.22\n'
        '- timeout: 50\n'
        '+ timeout: 20\n'
        '+ verbose: True\n'
    )
    assert generate_diff(file1_path, file2_path) == expected_diff
