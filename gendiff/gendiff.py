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
            # Ключ есть только во втором словаре
            result.append(f"  + {key}: {data_from_file2[key]}")
        elif key not in data_from_file2:
            # Ключ есть только в первом словаре
            result.append(f"  - {key}: {data_from_file1[key]}")
        elif data_from_file1[key] == data_from_file2[key]:
            # Ключ есть в обоих словарях с одинаковыми значениями
            result.append(f"    {key}: {data_from_file1[key]}")
        else:
            # Ключ есть в обоих словарях, но значения разные
            result.append(f"  - {key}: {data_from_file1[key]}")
            result.append(f"  + {key}: {data_from_file2[key]}")
    
    # Объединяем строки с переносами и добавляем фигурные скобки
    return "{\n" + "\n".join(result) + "\n}"


'''
if __name__ == '__main__':
    #difference = generate_diff(dict1, dict2)
    #print(difference)
    generate_diff(data1, data2)
'''
