import pytest
import json
import yaml
from gendiff.diff_gen import make_diff, generate_diff
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


def test_make_diff(json_data):
    data1, data2 = json_data
    diff = make_diff(data1, data2)
    assert diff == expected_diff


def test_generate_diff_json():
    diff = generate_diff(file1_json, file2_json, formatter=stylish)
    assert diff == stylish(expected_diff)


def test_generate_diff_yaml():
    diff = generate_diff(file1_yaml, file2_yaml, formatter=stylish)
    assert diff == stylish(expected_diff)
