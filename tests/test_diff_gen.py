import pytest
import json
import yaml
import os
from gendiff.generate_diff import make_diff, generate_diff
from gendiff.formatter import stylish


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


file1_json = os.path.join(FIXTURES_DIR, 'file1.json')
file2_json = os.path.join(FIXTURES_DIR, 'file2.json')


file1_yaml = os.path.join(FIXTURES_DIR, 'file1.yml')
file2_yaml = os.path.join(FIXTURES_DIR, 'file2.yml')


flat_file1_json = os.path.join(FIXTURES_DIR, 'flat_file1.json')
flat_file2_json = os.path.join(FIXTURES_DIR, 'flat_file2.json')


flat_file1_yaml = os.path.join(FIXTURES_DIR, 'flat_file1.yml')
flat_file2_yaml = os.path.join(FIXTURES_DIR, 'flat_file2.yml')


with open(os.path.join(FIXTURES_DIR, 'expected_diff.txt')) as f:
    expected_diff = json.load(f)


with open(os.path.join(FIXTURES_DIR, 'expected_plain_output.txt')) as f:
    expected_plain_output = f.read().strip()


with open(os.path.join(FIXTURES_DIR, 'expected_json_output.txt')) as f:
    expected_json_output = f.read().strip()


with open(os.path.join(FIXTURES_DIR, 'expected_flat_diff.txt')) as f:
    expected_flat_diff = f.read().strip()


@pytest.fixture
def json_data():
    with open(file1_json) as f1, open(file2_json) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
    return data1, data2


@pytest.fixture
def yaml_data():
    with open(file1_yaml) as f1, open(file2_yaml) as f2:
        data1 = yaml.safe_load(f1)
        data2 = yaml.safe_load(f2)
    return data1, data2


@pytest.fixture
def flat_json_data():
    with open(flat_file1_json) as f1, open(flat_file2_json) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
    return data1, data2


@pytest.fixture
def flat_yaml_data():
    with open(flat_file1_yaml) as f1, open(flat_file2_yaml) as f2:
        data1 = yaml.safe_load(f1)
        data2 = yaml.safe_load(f2)
    return data1, data2


def test_make_diff(json_data):
    data1, data2 = json_data
    diff = make_diff(data1, data2)
    assert diff == expected_diff


def test_generate_diff_json():
    diff = generate_diff(file1_json, file2_json, format_name='stylish')
    assert diff == stylish(expected_diff)


def test_generate_diff_yaml():
    diff = generate_diff(file1_yaml, file2_yaml, format_name='stylish')
    assert diff == stylish(expected_diff)


def test_generate_diff_plain():
    diff = generate_diff(file1_json, file2_json, format_name='plain')
    assert diff == expected_plain_output


def test_generate_diff_json_format():
    actual_diff_json = generate_diff(file1_json, file2_json, format_name='json')
    assert json.loads(actual_diff_json) == json.loads(expected_json_output)


def normalize_output(diff):
    return (diff.replace("False", "false").replace("True", "true")
                .replace(' ', '').replace('\n', ''))


def test_generate_diff_flat_json():
    diff = generate_diff(
        flat_file1_json, flat_file2_json, format_name='stylish'
    )
    normalized_diff = normalize_output(diff)
    normalized_expected = normalize_output(expected_flat_diff)
    assert normalized_diff == normalized_expected


def test_generate_diff_flat_yaml():
    diff = generate_diff(
        flat_file1_yaml, flat_file2_yaml, format_name='stylish'
    )
    normalized_diff = normalize_output(diff)
    normalized_expected = normalize_output(expected_flat_diff)
    assert normalized_diff == normalized_expected
