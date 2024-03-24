import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="path to files where we will find the text")
parser.add_argument("text", help="text which we are looking for")
parser.add_argument("--full", help="will be showed all places with founded text", action='store_true')
args = parser.parse_args()

print("This is a my path - ", args.path)
print("This is a my text - ", args.text)
print("This is a my version - ", args.full)


# open and find text
def open_and_find(path_to_file, text):
    date_from_file = []
    with open(path_to_file, 'r', encoding='utf-8') as open_file:
        data = open_file.read()
        lines = data.splitlines()
        count = 1
        for line in lines:
            if text in line:
                words = line.split()
                if text in words:
                    index = words.index(text)
                    start_index = max(index - 5, 0)
                    end_index = min(index + 6, len(words))
                    f_str = ''.join(words[start_index:end_index])
                    date_from_file.append([os.path.basename(path_to_file), count, f_str])
            count += 1
        return date_from_file


# go to the directory and open the file
def find_text(my_path, text):
    list1 = []
    list_dir = (next(os.walk(my_path))[2])
    files = [os.path.join(my_path, file) for file in list_dir]
    if not files:
        print("No any files")
        return []
    for file in files:
        result = open_and_find(file, text)
        list1.extend(result)
    return list1


my_path = args.path
text = args.text
res = find_text(my_path, text)


# display the text (depend on flag for --full argument)
def output_found_text():
    if args.full:
        print(res)
    else:
        print(res[0])


output_found_text()
