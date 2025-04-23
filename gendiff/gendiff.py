import json
import os


# Чтение JSON из файла (load)
def parse_files1():
    abs_path1 = os.path.abspath('file1.json')
    abs_path2 = os.path.abspath('file2.json')
    with open(abs_path1, "r", encoding="utf-8") as file:
        data_from_file1 = json.load(file)
    with open(abs_path2, "r", encoding="utf-8") as file:
        data_from_file2 = json.load(file)
    # print(data_from_file1)
    # print(data_from_file2)
    # print(data_from_file1, data_from_file2)
    return data_from_file1, data_from_file2


def generate_diff(data1, data2):    
    with open(data1, "r", encoding="utf-8") as file:
        data_from_file1 = json.load(file)
    with open(data2, "r", encoding="utf-8") as file:
        data_from_file2 = json.load(file)
    # print(data_from_file1)
    # print(data_from_file2)

# Получаем все уникальные ключи из обоих словарей и сортируем их
    all_keys = sorted(
    set(data_from_file1.keys()) | 
    set(data_from_file2.keys())
)
    
    result = []

    for key in all_keys:
        if key not in data_from_file1:
            value = format_value(data_from_file2[key])
            result.append(f"  + {key}: {value}")
        elif key not in data_from_file2:
            value = format_value(data_from_file1[key])
            result.append(f"  - {key}: {value}")
        elif data_from_file1[key] == data_from_file2[key]:
            value = format_value(data_from_file1[key])
            result.append(f"    {key}: {value}")
        else:
            value1 = format_value(data_from_file1[key])
            value2 = format_value(data_from_file2[key])
            result.append(f"  - {key}: {value1}")
            result.append(f"  + {key}: {value2}")
    
    return "{\n" + "\n".join(result) + "\n}"


# Вспомогательная функция для преобразования значений
def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()  # True → "true", False → "false"
    return value


'''
if __name__ == '__main__':
    #difference = generate_diff(dict1, dict2)
    #print(difference)
    generate_diff(data1, data2)
'''
