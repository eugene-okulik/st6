import argparse
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument("folderpath", help="Absolute path to folder with files")
# D:\AutoPy\st6\homework\eugene_okulik\data\logs
parser.add_argument("text", help="Text to search", type=str)
args = parser.parse_args()

folder_path = args.folderpath
files_list = os.listdir(folder_path)
search_txt = args.text

try:
    files_addresses = []
    for file in files_list:
        path = os.path.join(folder_path, file)
        files_addresses.append(path)

    for file in files_addresses:
        with open(file, 'r', encoding='utf-8') as opened_file:
            data_lines = opened_file.readlines()
            for index, line in enumerate(data_lines, 1):
                if search_txt in line:
                    print(f'Found {search_txt} in file {file} on line {index}.')

                    first_letter_index = line.index(search_txt)
                    last_letter_index = first_letter_index + len(search_txt)

                    start = first_letter_index - 50
                    end = last_letter_index + 51

                    if start < 0:
                        print('\n', line[:end])
                    elif end > len(line):
                        print('\n', line[start:])
                    else:
                        print('\n', line[start:end])
                else:
                    pass
except FileNotFoundError as err:
    print(err)
