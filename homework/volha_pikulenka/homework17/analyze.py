# import argparse
# import os
# import re
# import glob
#
# parser = argparse.ArgumentParser()
# parser.add_argument("folderpath", help="Absolute path to folder with files")
# # D:\AutoPy\st6\homework\eugene_okulik\data\logs
# parser.add_argument("text", help="Text to search", type=str)
# args = parser.parse_args()
#
# folder_path = args.folderpath
# files_list = os.listdir(folder_path)
# search_txt = args.text
#
# try:
#     files_addresses = []
#     for file in files_list:
#         path = os.path.join(folder_path, file)
#         files_addresses.append(path)
#
#     for file in files_addresses:
#         with open(file, 'r', encoding='utf-8') as opened_file:
#             data_lines = opened_file.readlines()
#             for line_index, line in enumerate(data_lines, 1):
#                 if search_txt in line:
#                     print(f'Found {search_txt} in file {file} on line {line_index}.')
#
#                     line_split = re.split(r'\s|,|:|"|\".\"|{|}|;|\(|\)|\[|]', line)
#                     for i in line_split:
#                         if i == '':
#                             line_split.remove(i)
#
#                     search_txt_prepare = search_txt.strip().split()
#
#                     if len(search_txt_prepare) > 1:
#
#                         search_txt_prepare = search_txt.strip().split()
#                         search_txt_split = re.split(r'\s|,|:|"|\".\"|{|}|:|;|\(|\)|\[|]|]', search_txt_prepare[-1])
#
#                         search_index = line_split.index(search_txt_split[-1])
#                         start = search_index - 10
#                         end = search_index + 11
#
#                         if start < 0:
#                             print('5 words before/after/searched word\n', line_split[:end])
#                         elif end > len(line_split):
#                             print('5 words before/after/searched word\n', line_split[start:])
#                         else:
#                             print('5 words before/after/searched word\n', line_split[start:end])
#                         break
#                     else:
#                         letter_index = line.index(search_txt_prepare[0])
#                         word_end = []
#                         word_start = []
#
#                         letter_index1 = letter_index
#                         letter_index2 = letter_index
#
#                         for letter in line:
#                             if line[letter_index1] != ',':
#                                 word_end.append(line[letter_index1])
#                                 letter_index1 += 1
#                             # движемся назад
#                             elif line[letter_index2] != ',':
#                                 letter_index2 -= 1
#                                 word_start.insert(0, line[letter_index2])
#                             else:
#                                 pass
#                         word = word_start + word_end
#                         found_word = "".join(word)
#                         strip_w = re.split(r'\s|,|:|"|\".\"|{|}|:|;|\(|\)|\[|]|]', found_word)
#                         word_start.remove(',')
#
#                         if strip_w[-1] in line_split:
#                             search_index = search_txt_prepare.index(strip_w[-1])
#                             print(search_index)
#
#                             start = search_index - 5
#                             end = search_index + 6
#
#                             if start < 0:
#                                 print('5 words before/after/searched word\n', line_split[:end])
#                             elif end > len(line_split):
#                                 print('5 words before/after/searched word\n', line_split[start:])
#                             else:
#                                 print('5 words before/after/searched word\n', line_split[start:end])
#                             break
#                         else:
#                             print('no match')
#                 else:
#                     pass
# except FileNotFoundError as err:
#     print(err)

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

                    # line_split = re.split(r'\s|,|:|"|\".\"|{|}|:|;|\(|\)|\[|]|]', line)
                    # for i in line_split:
                    #     if i == '':
                    #         line_split.remove(i)

                    # search_txt_prepare = search_txt.strip().split()
                    #
                    # search_txt_split = re.split(r'\s|,|:|"|\".\"|{|}|:|;|\(|\)|\[|]|]', search_txt_prepare[-1])
                    #
                    # search_index = line_split.index(search_txt_split[-1])
                    # # print(search_index)
                    # start = search_index - 1
                    # end = search_index + 2
                    #
                    # if start < 0:
                    #     print('5 words before/after/searched word\n', line_split[:end])
                    # elif end > len(line_split):
                    #     print('5 words before/after/searched word\n', line_split[start:])
                    # else:
                    #     print('5 words before/after/searched word\n', line_split[start:end])
                    # break
                else:
                    pass
except FileNotFoundError as err:
    print(err)
