import os
import argparse
from datetime import datetime


class ColoredHelpFormatter(argparse.HelpFormatter):
    def __init__(self, *args, **kwargs):
        super(ColoredHelpFormatter, self).__init__(*args, **kwargs)

    def add_argument(self, action):
        if action.dest == 'date':
            action.help = '\033[33m{}\033[0m'.format(action.help)  # желтый цвет
        elif action.dest == 'text':
            action.help = '\033[32m{}\033[0m'.format(action.help)  # зеленый цвет
        elif action.dest == 'unwanted':
            action.help = '\033[31m{}\033[0m'.format(action.help)  # красный цвет
        super(ColoredHelpFormatter, self).add_argument(action)


parser = argparse.ArgumentParser(formatter_class=ColoredHelpFormatter)
parser.add_argument("path", type=str, help="path to files where we will find the text")
parser.add_argument("--date", dest="date", action="store",
                    help="""Datetime for search:
                           - less than: "../2024-03-13 00:00:00.000"
                           - more than: "2024-03-13 00:00:00.000/.."
                           - from - to: "2024-03-13 00:00:00.000/2024-03-14 00:00:00.000"
                           - exact: "2024-03-13 00:00:00.000\"""")
parser.add_argument("--text", dest="text", help="text which we are looking for")
parser.add_argument("--unwanted", dest="unwanted", help='Choose the text condition')
parser.add_argument("--full", help="will be showed all places with founded text", action='store_true')
args = parser.parse_args()

path = args.path
text = args.text
unwanted = args.unwanted
date = args.date


# определить что указал пользователь: файл или папку
def check_path(path):
    if os.path.isdir(path):
        list_dir = (next(os.walk(path))[2])
        files = [os.path.join(path, file) for file in list_dir]
        if not files:
            print("No any files")
            return []
    else:
        files = [path]
    return files


# разбиваем весь файл на блоки
def open_and_parse_to_blocks(path_to_file):
    blocks = {}
    with open(path_to_file, 'r', encoding='utf-8') as open_file:
        data = open_file.read()
        lines = data.splitlines()
        block = ''
        for line in lines:
            try:
                current_date = datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S.%f')
                block = line
            except ValueError:
                continue
            else:
                block += line
                if current_date:
                    blocks[current_date] = block
    return blocks


# выбираем блоки с нужной датой
def find_by_date(date, new_block):
    date_blocks = {}
    if date.startswith("../"):  # less than
        current_date = datetime.strptime(date[3:], '%Y-%m-%d %H:%M:%S.%f')
        date_blocks = {key: value for key, value in new_block.items() if key < current_date}
    elif date.endswith("/.."):  # more than
        current_date = datetime.strptime(date[:-3], '%Y-%m-%d %H:%M:%S.%f')
        date_blocks = {key: value for key, value in new_block.items() if key > current_date}
    elif "/" in date:  # from - to
        start_date = datetime.strptime(date.split("/")[0], '%Y-%m-%d %H:%M:%S.%f')
        end_date = datetime.strptime(date.split("/")[1], '%Y-%m-%d %H:%M:%S.%f')
        date_blocks = {key: value for key, value in new_block.items() if start_date <= key <= end_date}
    elif "/" not in date:
        current_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        date_blocks = {key: value for key, value in new_block.items() if current_date == key}
    return date_blocks


# выбираем блоки с нужным текстом
def find_by_text(blocks, text=None, unwanted=None):
    founded_text = {}
    if text:
        founded_text = {key: value for key, value in blocks.items() if text in value}
    elif unwanted:
        founded_text = {key: value for key, value in blocks.items() if unwanted in value}
    return founded_text


def open_and_find(path, text=None, date=None, unwanted=None):
    date_from_file = {}
    count_block = 0
    count_res = 0
    files = check_path(path)
    for file in files:
        new_block = open_and_parse_to_blocks(file)
        count_block += len(new_block)
        if date or text or unwanted:
            if date:
                new_block = find_by_date(date, new_block)
            if text:
                new_block = find_by_text(new_block, text)
            if unwanted:
                unwanted_blocks = find_by_text(new_block, unwanted=unwanted)
                for key in unwanted_blocks:
                    del new_block[key]
        date_from_file.update(new_block)
    count_res += len(date_from_file)
    return date_from_file, count_block, count_res


def cut_message_for_text(text):
    res = open_and_find(path, text, date, unwanted)[0]
    for key, value in res.items():
        message_parts = value.split(text, 1)
        if len(message_parts) > 1:
            formatted_text = '\033[32m{}\033[0m'.format(text)
            formatted_key = '\033[33m{}\033[0m'.format(key)
            str = message_parts[0][-150:] + formatted_text + message_parts[1][:150]
            print(formatted_key, str)


# вывод текста
def display_result(path, text, date, unwanted):
    if args.text:
        print('\033[32mText to search:\033[0m', args.text)
    if args.date:
        print('\033[33mDate condition:\033[0m', args.date)
    if args.unwanted:
        print('\033[31mUnwanted text:\033[0m', args.unwanted)

    res, count_block, count_res = open_and_find(path, text, date, unwanted)
    if args.text and args.full:
        print(res)
    elif args.text and args.full is False:
        cut_message_for_text(text)
    else:
        if args.full:
            print(res)
        else:
            for key, value in res.items():
                formatted_key = f"\033[33m{key}\033[0m"
                print(formatted_key, value[:300])

    print(f"\033[33mTotal logs count: \033[0m\033[34m{count_block}\033[0m")
    print(f"\033[33mTotal result count: \033[0m\033[34m{count_res}\033[0m")


display_result(path, text, date, unwanted)
