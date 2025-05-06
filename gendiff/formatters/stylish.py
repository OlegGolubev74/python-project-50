def format_diff(diff, depth=0):
    lines = []
    indent = " " * (depth * 4)

    for node in diff:
        key = node["key"]
        type_ = node["type"]
        
        if type_ == "nested":
            lines.append(f"{indent}    {key}: {{")
            lines.append(format_diff(node["children"], depth + 1))
            lines.append(f"{indent}    }}")
        elif type_ == "added":
            value = format_value(node["value"], depth + 1)
            lines.append(f"{indent}  + {key}: {value}")
        elif type_ == "removed":
            value = format_value(node["value"], depth + 1)
            lines.append(f"{indent}  - {key}: {value}")
        elif type_ == "changed":
            old_value = format_value(node["old_value"], depth + 1)
            new_value = format_value(node["new_value"], depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
        elif type_ == "unchanged":
            value = format_value(node["value"], depth + 1)
            lines.append(f"{indent}    {key}: {value}")

    return "\n".join(lines)


def format_value(value, depth):
    if isinstance(value, dict):
        lines = ["{"]
        inner_indent = " " * ((depth + 1) * 4)
        for k, v in value.items():
            lines.append(f"{inner_indent}{k}: {format_value(v, depth + 1)}")
        lines.append(" " * (depth * 4) + "}")
        return "\n".join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    return str(value)


def render(diff):
    return "{\n" + format_diff(diff) + "\n}"