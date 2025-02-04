import re
import unicodedata
from os import makedirs
from json import dump
from constants import __DATA_BASE_DIR

def convert_directory_name(tournament):
    
    normalized_string = unicodedata.normalize('NFKD', tournament).encode('ASCII', 'ignore').decode('utf-8')
    
    directory_name = re.sub(r'\s+', '_', normalized_string)
    
    directory_name = re.sub(r'[^\w_]', '', directory_name)
    
    directory_name = directory_name.lower()
    
    return directory_name

def create_directory(tournament, year):

    directory_to_create = convert_directory_name(tournament)
    directory_to_create = f'{directory_to_create}/{year}'

    makedirs(f'{__DATA_BASE_DIR}{directory_to_create}', exist_ok=True)

    return directory_to_create

def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as json_file:
        dump(data, json_file, ensure_ascii=False, indent=4)