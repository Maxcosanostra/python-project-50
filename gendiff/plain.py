def format_plain(diff):
    lines = []
    process_diff(diff, lines)
    return '\n'.join(lines)


def process_diff(node, lines, parent=''):
    for key, value in sorted(node.items()):
        full_path = f"{parent}.{key}" if parent else key
        if isinstance(value, dict) and 'type' not in value:
            process_diff(value, lines, full_path)
        else:
            result = format_node(full_path, value)
            if result:
                lines.append(result)


def format_node(full_path, node):
    status = node['type']
    if status == 'added':
        return (
            f"Property '{full_path}' was added with value: "
            f"{format_value(node['value'])}"
        )
    elif status == 'removed':
        return f"Property '{full_path}' was removed"
    elif status == 'changed':
        return (
            f"Property '{full_path}' was updated. "
            f"From {format_value(node['old_value'])} "
            f"to {format_value(node['new_value'])}"
        )
    elif status == 'nested':
        nested_lines = []
        process_diff(node['children'], nested_lines, full_path)
        return '\n'.join(nested_lines)
    return ''


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)
