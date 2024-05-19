from gendiff.parsing import read_file


def make_diff(data1, data2):
    diff = {}
    keys = set(data1.keys()) | set(data2.keys())

    for key in sorted(keys):
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            diff[f'  {key}'] = value1
        elif key not in data1:
            diff[f'+ {key}'] = value2
        elif key not in data2:
            diff[f'- {key}'] = value1
        else:
            diff[f'- {key}'] = value1
            diff[f'+ {key}'] = value2

    return diff


def setup_diff(diff):
    result = ['{']
    for key, value in diff.items():
        if isinstance(value, bool):
            value = str(value).lower()
        elif isinstance(value, str):
            value = f'"{value}"'
        result.append(f'\n  {key}: {value}')
    result.append('\n}')
    return ''.join(result)


def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = make_diff(data1, data2)
    return setup_diff(diff)
