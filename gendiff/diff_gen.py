from gendiff.parsing import read_file
from gendiff.formatter import stylish


def make_diff(data1, data2):
    diff = {}
    keys = set(data1.keys()) | set(data2.keys())

    for key in sorted(keys):
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key not in data1:
            diff[key] = {'type': 'added', 'value': value2}
        elif key not in data2:
            diff[key] = {'type': 'removed', 'value': value1}
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = {
                'type': 'nested',
                'children': make_diff(value1, value2)
            }
        elif value1 != value2:
            diff[key] = {
                'type': 'changed',
                'old_value': value1,
                'new_value': value2
            }
        else:
            diff[key] = {'type': 'unchanged', 'value': value1}

    return diff


def generate_diff(file_path1, file_path2, formatter=stylish):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = make_diff(data1, data2)
    return formatter(diff)
