def convert_to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff, parent_key=''):
    lines = []
    
    for node in diff:
        key = node['key']
        full_path = f"{parent_key}{key}"
        type_ = node['type']
        
        if type_ == 'nested':
            lines.append(format_plain(node['children'], f"{full_path}."))
        elif type_ == 'added':
            value = convert_to_str(node['value'])
            lines.append(
                f"Property '{full_path}' was added "
                f"with value: {value}"
            )
        elif type_ == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        elif type_ == 'changed':
            old_value = convert_to_str(node['old_value'])
            new_value = convert_to_str(node['new_value'])
            lines.append(
                f"Property '{full_path}' was updated. " 
                f"From {old_value} to {new_value}"
            )
            
    return '\n'.join(lines)


def render(diff):
    return format_plain(diff)