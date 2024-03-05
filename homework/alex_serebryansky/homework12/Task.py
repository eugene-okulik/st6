import os
import re

from dateutil import parser
from dateutil.parser import ParserError


def parse_str_date_to_dateformat(date: str):
    pattern = ("\\d{4}-\\d{2}-\\d{2}|\\d{2}-\\d{2}-\\d{4}|"
               "\\d{4}.\\d{2}.\\d{2}|\\d{2}.\\d{2}.\\d{4}|"
               "\\d{4}/\\d{2}/\\d{2}|\\d{2}/\\d{2}/\\d{4}")

    try:
        date_line = ''.join(re.findall(pattern, date))
        return parser.parse(date_line)
    except ParserError as err:
        print('Error: {}'.format(err))
        return ("The following date formats are supported:"
                "\nYYYY-MM-DD, YYYY.MM.DD, YYYY/MM/DD"
                "\nDD-MM-YYYY, DD.MM.YYYY, DD/MM/YYYY")


input_date = input('Enter date in YYYY-MM-DD format: ')
print(parse_str_date_to_dateformat(input_date))

""" Task 2 """
path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'eugene_okulik', 'hw_12', 'data.txt')
with open(path, "r", encoding="utf-8") as file:

    upper_char = list(filter(lambda char: char if char.isupper() else None, list(file.read())))
print(upper_char)
