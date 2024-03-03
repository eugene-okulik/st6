import os
import datetime


path_to_repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
path_to_file = os.path.join(path_to_repo, 'homework', 'eugene_okulik', 'hw_13', 'data.txt')

with open(path_to_file, 'r', encoding='UTF-8') as open_file:
    data = open_file.read()
    print(data)

for line in data.split('\n'):
    numbers, dates, time, *action = line.split()
    number = numbers.strip('.')
    date = datetime.datetime.strptime(f'{dates} {time}', '%Y-%m-%d %H:%M:%S.%f')
    if number == '1':
        print(f'Дата на неделю позже: {date + datetime.timedelta(weeks=1)}')
    elif number == '2':
        print(f'День недели будет: {date.strftime('%A')}')
    elif number == '3':
        days_ago = datetime.datetime.now() - date
        print(f'{days_ago.days} дней назад была эта неделя')
