import os
import magic

mime = magic.Magic(mime=True)

files_with_types:dict[str, str] = {}

def cleaner(path: str):
    create_file_list(path)
    
    
    
def create_file_list(path: str):
    dir_list = os.listdir(path)

    for file in dir_list:
        file_type = mime.from_file(f'{path}/{file}')
        files_with_types[file_type] = file
        # print(os.path.splitext(file))
    
    print(files_with_types)   
    return "Done"
