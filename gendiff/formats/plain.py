def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)


def make_plain_result(diff):
    def _iter(diff, path=''):
        res = []
        for key, data in diff.items():
            current_path = f'{path}.{key}' if path else key
            match data['type']:
                case 'added':
                    value = to_str(data['value'])
                    res.append(
                        f"Property '{current_path}' "
                        f"was added with value: {value}"
                    )
                case 'removed':
                    res.append(f"Property '{current_path}' was removed")
                case 'changed':
                    old_value = to_str(data['old_value'])
                    new_value = to_str(data['new_value'])
                    res.append(
                        f"Property '{current_path}' was updated. "
                        f"From {old_value} to {new_value}"
                    )
                case 'nested':
                    res.extend(_iter(data['children'], current_path))
                case 'unchanged':
                    continue
                case _:
                    raise ValueError(
                        f"Unsupported node type at path "
                        f"'{current_path}': {data['type']}"
                    )
        return res

    return '\n'.join(_iter(diff))
