import os
import datetime


def updated_date_format(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')


def print_date_week_later(date):
    week_later = datetime.timedelta(weeks=1)
    print(date + week_later)


def print_week_day(date):
    match date.weekday():
        case 0:
            print('Monday')
        case 1:
            print('Tuesday')
        case 2:
            print('Wednsday')
        case 3:
            print('THursday')
        case 4:
            print('Friday')
        case 5:
            print('Saturday')
        case 6:
            print('Sunday')


def print_how_many_days_ago(date):
    now = datetime.datetime.now()
    days_delta = now - date
    print(days_delta)


repo_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
path_to_file = os.path.join(repo_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(path_to_file, 'r', encoding='utf-8') as opened_file:
    data = opened_file.read()

lines = data.splitlines()

iter = 0
for line in lines:
    date_line = line[3:29]
    date = updated_date_format(date_line)
    iter += 1
    if iter == 1:
        print_date_week_later(date)
    elif iter == 2:
        print_week_day(date)
    elif iter == 3:
        print_how_many_days_ago(date)
    else:
        break
