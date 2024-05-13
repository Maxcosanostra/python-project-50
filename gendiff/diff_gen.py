import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

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

    result = ['{\n']
    for key, value in diff.items():
        result.append(f'  {key}: {value}\n')
    result.append('}')
    return ''.join(result)
