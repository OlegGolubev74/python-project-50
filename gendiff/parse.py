import json
from pathlib import Path



def parse(file_path):
    return json.load(open(file_path))
