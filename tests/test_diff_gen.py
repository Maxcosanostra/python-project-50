import pytest
import json
import yaml
from gendiff.generate_diff import make_diff, generate_diff
from gendiff.formatter import stylish
import os


file1_json = os.path.join(
    os.path.dirname(__file__), '../gendiff/files/file1.json'
)
file2_json = os.path.join(
    os.path.dirname(__file__), '../gendiff/files/file2.json'
)
file1_yaml = os.path.join(
    os.path.dirname(__file__), '../gendiff/files/file1.yml'
)
file2_yaml = os.path.join(
    os.path.dirname(__file__), '../gendiff/files/file2.yml'
)
flat_file1_json = os.path.join(
    os.path.dirname(__file__), '../gendiff/files/flat_file1.json'
)
flat_file2_json = os.path.join(
    os.path.dirname(__file__), '../gendiff/files/flat_file2.json'
)
flat_file1_yaml = os.path.join(
    os.path.dirname(__file__), '../gendiff/files/flat_file1.yml'
)
flat_file2_yaml = os.path.join(
    os.path.dirname(__file__), '../gendiff/files/flat_file2.yml'
)


expected_diff = {
    "common": {
        "type": "nested",
        "children": {
            "follow": {"type": "added", "value": False},
            "setting1": {"type": "unchanged", "value": "Value 1"},
            "setting2": {"type": "removed", "value": 200},
            "setting3": {
                "type": "changed",
                "old_value": True,
                "new_value": None
            },
            "setting4": {"type": "added", "value": "blah blah"},
            "setting5": {"type": "added", "value": {"key5": "value5"}},
            "setting6": {
                "type": "nested",
                "children": {
                    "doge": {
                        "type": "nested",
                        "children": {
                            "wow": {
                                "type": "changed",
                                "old_value": "",
                                "new_value": "so much"
                            }
                        },
                    },
                    "key": {"type": "unchanged", "value": "value"},
                    "ops": {"type": "added", "value": "vops"},
                },
            },
        },
    },
    "group1": {
        "type": "nested",
        "children": {
            "baz": {"type": "changed", "old_value": "bas", "new_value": "bars"},
            "foo": {"type": "unchanged", "value": "bar"},
            "nest": {
                "type": "changed",
                "old_value": {"key": "value"},
                "new_value": "str"
            },
        },
    },
    "group2": {
        "type": "removed",
        "value": {"abc": 12345, "deep": {"id": 45}}
    },
    "group3": {
        "type": "added",
        "value": {"deep": {"id": {"number": 45}}, "fee": 100500},
    },
}


expected_plain_output = (
    "Property 'common.follow' was added with value: false\n"
    "Property 'common.setting2' was removed\n"
    "Property 'common.setting3' was updated. From true to null\n"
    "Property 'common.setting4' was added with value: 'blah blah'\n"
    "Property 'common.setting5' was added with value: [complex value]\n"
    "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'\n"
    "Property 'common.setting6.ops' was added with value: 'vops'\n"
    "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
    "Property 'group1.nest' was updated. From [complex value] to 'str'\n"
    "Property 'group2' was removed\n"
    "Property 'group3' was added with value: [complex value]"
)


expected_json_output = json.dumps(expected_diff, indent=2, sort_keys=True)


expected_flat_diff = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


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
    print("Actual plain output:\n", diff)
    assert diff == expected_plain_output


def test_generate_diff_json_format():
    actual_diff_json = generate_diff(file1_json, file2_json, format_name='json')
    assert json.loads(actual_diff_json) == json.loads(expected_json_output)


def normalize_output(diff):
    return diff.replace("False", "false").replace("True", "true")\
               .replace(' ', '').replace('\n', '')


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
