import argparse
import os
import datetime
import re


parser = argparse.ArgumentParser()
parser.add_argument("path", help="Path to file or folder with files")
# D:\AutoPy\st6\homework\eugene_okulik\data\logs
parser.add_argument("--text", help="Text to search", type=str)
parser.add_argument("--unwantedtext", help="Search blocks were text doesn't appear", type=str)
parser.add_argument("--date",
                    help="""Date to search,
                    -greater than '>2024-04-07 00:00:00.000'
                    -less than '<2024-04-07 00:00:00.000'
                    -exact date '=2024-04-07 00:00:00.000'
                    -period '2024-04-07 00:00:00.000/2025-04-07 00:00:00.000""",
                    type=str)

args = parser.parse_args()

path = args.path
date = args.date
text = args.text
unwanted = args.unwantedtext
full = args.full


def list_files(path):
    """List files in the specified directory."""
    if os.path.isdir(path):
        return [os.path.join(path, file) for file in os.listdir(path)]
    elif os.path.isfile(path):
        return [path]
    else:
        raise FileNotFoundError("Specified path is neither a file nor a directory.")


def split_text_by_date(text):
    date_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+'
    date_matches = re.finditer(date_pattern, text)
    blocks = []
    start_index = 0
    for match in date_matches:
        end_index = match.start()
        if start_index != end_index:
            blocks.append(text[start_index:end_index].strip())
        start_index = match.start()
    blocks.append(text[start_index:].strip())
    return blocks


try:
    files_addresses = list_files(args.path)
    for file_path in files_addresses:

        with open(file_path, 'r', encoding='utf-8') as opened_file:
            data = opened_file.read()

        blocks = split_text_by_date(data)

        if text is not None:
            for i in blocks:
                if text in i:
                    print(i[:100])

        if unwanted is not None:
            for i in blocks:
                if unwanted not in i:
                    print(i[:100])

        if date is not None:
            for i in blocks:
                block_date = datetime.datetime.strptime(i[:23], '%Y-%m-%d %H:%M:%S.%f')
                if date[0] in ['>', '<', '=']:
                    operation = date[0]
                    given_date = datetime.datetime.strptime(date[1:], '%Y-%m-%d %H:%M:%S.%f')
                    if operation == '>' and block_date > given_date:
                        print(i[:100])
                    elif operation == '<' and block_date < given_date:
                        print(i[:100])
                    elif operation == '=' and block_date == given_date:
                        print(i[:100])
                elif date[23] == '/':
                    given_date_from = datetime.datetime.strptime(date[:23], '%Y-%m-%d %H:%M:%S.%f')
                    given_date_to = datetime.datetime.strptime(date[24:], '%Y-%m-%d %H:%M:%S.%f')
                    if block_date > given_date_from and block_date < given_date_to:
                        print(i[:100])

except (FileNotFoundError, ValueError) as err:
    print(err)
