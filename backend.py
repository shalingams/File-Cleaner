import os
import magic
import shutil

mime = magic.Magic(mime=True)

files_with_types: dict[list, list] = {}

def cleaner(path: str):
    clean_up(path)
    
    
    
def clean_up(path: str):
    dir_list = (
        file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))
    )
    for file in dir_list:
        file_type = mime.from_file(f"{path}/{file}")
        if not os.path.exists(f'{path}/{file_type}'):
            os.makedirs(f"{path}/{file_type}")
            
        shutil.move(f"{path}/{file}", f"{path}/{file_type}/{file}")
