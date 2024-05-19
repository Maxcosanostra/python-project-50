import pytest
from gendiff.diff_gen import generate_diff


@pytest.fixture
def json_file1_path():
    return 'file1.json'


@pytest.fixture
def json_file2_path():
    return 'file2.json'


@pytest.fixture
def yaml_file1_path():
    return 'file1.yml'


@pytest.fixture
def yaml_file2_path():
    return 'file2.yml'


def test_generate_diff_json(json_file1_path, json_file2_path):
    expected_diff = (
        '{\n'
        '  - follow: false\n'
        '    host: "hexlet.io"\n'
        '  - proxy: "123.234.53.22"\n'
        '  - timeout: 50\n'
        '  + timeout: 20\n'
        '  + verbose: true\n'
        '}'
    )
    assert generate_diff(json_file1_path, json_file2_path) == expected_diff


def test_generate_diff_yaml(yaml_file1_path, yaml_file2_path):
    expected_diff = (
        '{\n'
        '  - follow: false\n'
        '    host: "hexlet.io"\n'
        '  - proxy: "123.234.53.22"\n'
        '  - timeout: 50\n'
        '  + timeout: 20\n'
        '  + verbose: true\n'
        '}'
    )
    assert generate_diff(yaml_file1_path, yaml_file2_path) == expected_diff


def test_generate_diff_json_yaml(json_file1_path, yaml_file2_path):
    expected_diff = (
        '{\n'
        '  - follow: false\n'
        '    host: "hexlet.io"\n'
        '  - proxy: "123.234.53.22"\n'
        '  - timeout: 50\n'
        '  + timeout: 20\n'
        '  + verbose: true\n'
        '}'
    )
    assert generate_diff(json_file1_path, yaml_file2_path) == expected_diff


def test_generate_diff_yaml_json(yaml_file1_path, json_file2_path):
    expected_diff = (
        '{\n'
        '  - follow: false\n'
        '    host: "hexlet.io"\n'
        '  - proxy: "123.234.53.22"\n'
        '  - timeout: 50\n'
        '  + timeout: 20\n'
        '  + verbose: true\n'
        '}'
    )
    assert generate_diff(yaml_file1_path, json_file2_path) == expected_diff
