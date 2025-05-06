from gendiff.parsing_files import parse

from gendiff.formatters.stylish import render as stylish
from gendiff.formatters.plain import render as plain
from gendiff.formatters.json import render as json_format


def generate_diff(file1, file2, format_name='stylish'):
    data1, data2 = parse(file1, file2)
    diff = build_diff(data1, data2)
    if format_name == 'stylish':
        return stylish(diff)
    elif format_name == 'plain':
         return plain(diff)
    elif format_name == 'json':
        return json_format(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")


def build_diff(data1, data2):
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        if key not in data1:
            diff.append({
                "key": key,
                "type": "added",
                "value": data2[key]
            })
        elif key not in data2:
            diff.append({
                "key": key,
                "type": "removed",
                "value": data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                "key": key,
                "type": "nested",
                "children": build_diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            diff.append({
                "key": key,
                "type": "unchanged",
                "value": data1[key]
            })
        else:
            diff.append({
                "key": key,
                "type": "changed",
                "old_value": data1[key],
                "new_value": data2[key]
            })
    return diff
