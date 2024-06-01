def format_value(value, depth):
    if isinstance(value, dict):
        lines = []
        indent = ' ' * (depth + 4)
        for key, val in value.items():
            lines.append(f"{indent}{key}: {format_value(val, depth + 4)}")
        joined_lines = '\n'.join(lines)
        return '{\n' + joined_lines + '\n' + ' ' * depth + '}'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def format_line(key, value, depth, prefix="  "):
    indent = ' ' * depth
    return f"{indent}{prefix}{key}: {value}"


def process_node(key, node, depth):
    if node['type'] == 'added':
        return format_line(
            key, format_value(node['value'], depth + 4), depth, prefix="+ "
        )

    elif node['type'] == 'removed':
        return format_line(
            key, format_value(node['value'], depth + 4), depth, prefix="- "
        )

    elif node['type'] == 'unchanged':
        return format_line(
            key, format_value(node['value'], depth + 4), depth
        )

    elif node['type'] == 'changed':
        old_value = format_value(node['old_value'], depth + 4)
        new_value = format_value(node['new_value'], depth + 4)
        return [
            format_line(key, old_value, depth, prefix="- "),
            format_line(key, new_value, depth, prefix="+ ")
        ]

    elif node['type'] == 'nested':
        nested_diff = make_stylish_result(node['children'], depth + 4)
        return f"{' ' * depth}  {key}: {nested_diff}"


def make_stylish_result(diff, depth=0):
    lines = []
    for key, node in sorted(diff.items()):
        if node['type'] == 'nested':
            value = make_stylish_result(node['children'], depth + 4)
            lines.append(
                f"{' ' * (depth + 2)}  {key}: {value}"
            )

        elif node['type'] == 'added':
            lines.append(
                f"{' ' * (depth + 2)}+ {key}: "
                f"{format_value(node['value'], depth + 4)}"
            )

        elif node['type'] == 'removed':
            lines.append(
                f"{' ' * (depth + 2)}- {key}: "
                f"{format_value(node['value'], depth + 4)}"
            )

        elif node['type'] == 'unchanged':
            lines.append(
                f"{' ' * (depth + 2)}  {key}: "
                f"{format_value(node['value'], depth + 4)}"
            )

        elif node['type'] == 'changed':
            old_value = format_value(node['old_value'], depth + 4)
            new_value = format_value(node['new_value'], depth + 4)
            lines.append(
                f"{' ' * (depth + 2)}- {key}: {old_value}"
            )
            lines.append(
                f"{' ' * (depth + 2)}+ {key}: {new_value}"
            )

    result = "{\n" + "\n".join(lines) + f"\n{' ' * depth}}}"
    return result
