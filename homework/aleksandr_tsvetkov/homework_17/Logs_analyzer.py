import os
import argparse
import datetime
from colorama import init, Fore, Style

init()

parser = argparse.ArgumentParser()
parser.add_argument('file', help='Logs_Analyzer.py with path to logs, e.x '
                                 'Z:/GitHub/st6/homework/eugene_okulik/data/logs')
parser.add_argument('--search_date', help='date for search in format YYYY-MM-DD HH:MM:SS.000, ex. '
                                          '"2022-02-03 00:01:13.623"')
parser.add_argument('--search_text', help='text for search in logs')
parser.add_argument('--full', action='store_true', help='displays 5 words before and after the found text')
args = parser.parse_args()


def search_in_logs(file, search_date, search_text, full):
    error_printed = False
    for filename in os.listdir(file):
        file_path = os.path.join(file, filename)
        with open(file_path, 'r', encoding='UTF-8') as open_file:
            data = open_file.readlines()
            line_number = 0
            for line in data:
                line_number += 1
                try:
                    if search_date:
                        date = datetime.datetime.strptime(search_date, '%Y-%m-%d %H:%M:%S.%f')
                        date_str = date.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                        if date_str in line:
                            print(f'File with date {search_date}: {filename}')
                except ValueError:
                    if not error_printed:
                        print(Fore.RED + 'Invalid date format. Use format YYYY-MM-DD HH:MM:SS.000, '
                                         'ex. "2022-02-03 00:01:13.623"' + Style.RESET_ALL)
                        error_printed = True
                if search_text:
                    if search_text in line:
                        print(f'File with text: {search_text}: File name: {filename}, line number: {line_number+1}')
                        if full:
                            words = line.split()
                            index = words.index(search_text)
                            start_index = index - 5 if index - 5 > 0 else 0
                            end_index = index + 6 if index + 6 < len(words) else len(words)
                            print(' '.join(words[start_index:end_index]))


search_in_logs(args.file, args.search_date, args.search_text, args.full)
