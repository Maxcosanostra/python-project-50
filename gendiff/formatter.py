def format_value(value, depth):
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            indent = '  ' * (depth + 1)
            lines.append(f"{indent}{key}: {format_value(val, depth + 1)}")
        joined_lines = '\n'.join(lines)
        return '{\n' + joined_lines + '\n' + '  ' * depth + '}'
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def format_line(key, value, indent):
    return f"{indent}{key}: {value}"


def process_node(key, node, depth):
    indent = '  ' * depth
    if node['type'] == 'added':
        result = format_line(
            f"+ {key}",
            format_value(node['value'], depth + 1),
            indent
        )
    elif node['type'] == 'removed':
        result = format_line(
            f"- {key}",
            format_value(node['value'], depth + 1),
            indent
        )
    elif node['type'] == 'unchanged':
        result = format_line(
            f"  {key}",
            format_value(node['value'], depth + 1),
            indent
        )
    elif node['type'] == 'changed':
        old_value = format_value(node['old_value'], depth + 1)
        new_value = format_value(node['new_value'], depth + 1)
        result = [
            format_line(f"- {key}", old_value, indent),
            format_line(f"+ {key}", new_value, indent)
        ]
    elif node['type'] == 'nested':
        nested_diff = stylish(node['children'], depth + 1)
        result = format_line(
            f"  {key}",
            nested_diff,
            indent
        )
    return result


def stylish(diff, depth=0):
    lines = []
    for key, node in sorted(diff.items()):
        processed = process_node(key, node, depth)
        if isinstance(processed, list):
            lines.extend(processed)
        else:
            lines.append(processed)
    joined_lines = '\n'.join(lines)
    return '{\n' + joined_lines + '\n' + '  ' * depth + '}'
