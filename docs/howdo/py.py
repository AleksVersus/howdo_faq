import os
import re

def get_yml(sidebar_position:int) -> list:
    l = [
        '---\n',
        f'sidebar_position: {sidebar_position}\n',
        '---\n',
        '\n'
    ]
    return l

def remake_file(file_path:str) -> None:
    # file_path — abspath
    folder, file = os.path.split(file_path)
    file_name, file_ext = os.path.splitext(file)
    # extract number
    match = re.match(r'^(\d+)_(\w+)_(\d+)$', file_name)
    if match is not None:
        sidebar_position = int(match.group(1))
        with open(file_path, 'r', encoding='utf-8') as fp:
            file_lines = fp.readlines()
        yml = get_yml(sidebar_position)
        yml.extend(file_lines)
        new_file_path = os.path.join(folder, f'{match.group(2)}{file_ext}')
        with open(new_file_path, 'w', encoding='utf-8') as fp:
            fp.writelines(yml)
        os.remove(file_path)

def folder_view(folder_path:str) -> None:
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            remake_file(file_path)
        
def main():
    content = os.path.abspath('..\\informarch')
    folders = os.listdir(content)
    for folder in folders:
        folder_path = os.path.join(content, folder)
        if os.path.isdir(folder_path):
            folder_view(folder_path)

if __name__ == '__main__':
    main()