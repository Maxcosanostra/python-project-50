import pytest
from gendiff.formats.json import make_json_result
from gendiff.formats.plain import make_plain_result
from gendiff.formats.stylish import make_stylish_result
import json


@pytest.mark.parametrize("diff, formatter, expected_output", [
    (
        {"key": {"type": "added", "value": "value"}},
        "json",
        json.dumps({"key": {"type": "added", "value": "value"}}, indent=2)
    ),
    (
        {"key": {"type": "added", "value": "value"}},
        "plain",
        "Property 'key' was added with value: 'value'"
    ),
    (
        {"key": {"type": "added", "value": "value"}},
        "stylish",
        "{\n  + key: value\n}"
    ),
])
def test_format_diff(diff, formatter, expected_output):
    if formatter == "json":
        assert make_json_result(diff) == expected_output
    elif formatter == "plain":
        assert make_plain_result(diff) == expected_output
    elif formatter == "stylish":
        assert make_stylish_result(diff) == expected_output
