import json
import os

import yaml


def parse(data1, data2):
    file1_extension = os.path.splitext(data1)[1][1:]
    file2_extension = os.path.splitext(data2)[1][1:]
    if file1_extension == 'json' and file2_extension == 'json':
        with open(data1, "r", encoding="utf-8") as file:
            data_from_file1 = json.load(file)
        with open(data2, "r", encoding="utf-8") as file:
            data_from_file2 = json.load(file)

    if (file1_extension in ('yaml', 'yml') 
            and file2_extension in ('yaml', 'yml')):
        with open(data1, "r", encoding="utf-8") as file:
            data_from_file1 = yaml.safe_load(file)
        with open(data2, "r", encoding="utf-8") as file:
            data_from_file2 = yaml.safe_load(file)
    return (data_from_file1, data_from_file2)