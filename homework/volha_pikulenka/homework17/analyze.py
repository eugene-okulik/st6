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

                    line_split = re.split(r'\s|,|:|"|\".\"|{|}|:|;|\(|\)|\[|]|]', line)
                    for i in line_split:
                        if i == '':
                            line_split.remove(i)

                    search_txt_prepare = search_txt.strip().split()
                    search_txt_split = re.split(r'\s|,|:|"|\".\"|{|}|:|;|\(|\)|\[|]|]', search_txt_prepare[-1])

                    search_index = line_split.index(search_txt_split[-1])
                    start = search_index - 5
                    end = search_index + 6

                    if start < 0:
                        print('5 words before/after/searched word\n', line_split[:(end)])
                    elif end > len(line_split):
                        print('5 words before/after/searched word\n', line_split[start:])
                    else:
                        print('5 words before/after/searched word\n', line_split[start:end])
                    break
                else:
                    pass
except FileNotFoundError as err:
    print(err)
