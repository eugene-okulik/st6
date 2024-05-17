import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('path', help='path to log-files')
parser.add_argument('phrase', help='search phrase', type=str)
args = parser.parse_args()

dir_path = args.path
files_list = os.listdir(dir_path)
search_phrase = args.phrase

for file_name in files_list:
    abs_file_path = os.path.join(dir_path, file_name)
    with open(abs_file_path, 'r', encoding='utf-8') as _file:
        rows = _file.readlines()
        for row_number, row in enumerate(rows, 1):
            if search_phrase in row:
                index_before = row.index(search_phrase) - 100
                index_after = row.index(search_phrase) + len(search_phrase) + 100

                if index_before < 0:
                    print(f'File: {file_name}\nLine: {row_number}: {row[:index_after]}...\n')
                elif index_after > len(row):
                    print(f'File: {file_name}\nLine: {row_number}: ...{row[index_before:]}\n')
                else:
                    print(f'File: {file_name}\nLine: {row_number}: ...{row[index_before:index_after]}...\n')
            else:
                pass

# python analyzer.py /Users/alexs/autocourse/st6/homework/eugene_okulik/data/logs ERROR
