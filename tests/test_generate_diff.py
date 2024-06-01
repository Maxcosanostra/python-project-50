import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("file1, file2, formatter, expected_output", [
    (
        "file1.json", "file2.json", "stylish",
        "tests/fixtures/expected_diff.txt"
    ),
    (
        "file1.yml", "file2.yml", "stylish",
        "tests/fixtures/expected_diff.txt"
    ),
    (
        "file1.json", "file2.json", "plain",
        "tests/fixtures/expected_plain_output.txt"
    ),
    (
        "file1.yml", "file2.yml", "plain",
        "tests/fixtures/expected_plain_output.txt"
    ),
    (
        "file1.json", "file2.json", "json",
        "tests/fixtures/expected_json_output.txt"
    ),
    (
        "file1.yml", "file2.yml", "json",
        "tests/fixtures/expected_json_output.txt"
    ),
])
def test_generate_diff(file1, file2, formatter, expected_output):
    with open(expected_output) as f:
        expected = f.read().strip()
    result = generate_diff(file1, file2, formatter)
    print(f"Expected:\n{expected}")
    print(f"Result:\n{result}")
    assert result == expected
