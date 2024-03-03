import os
from datetime import datetime, timedelta

repo_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

path_to_file = os.path.join(repo_path, 'st6', 'homework', 'eugene_okulik', 'hw_13', 'data.txt')

with open(path_to_file, 'r', encoding='utf-8') as open_file:
    data = open_file.read()
    lines = data.splitlines()
    date_from_file = []
    for i in lines:
        start_index = 3
        end_symbol = ' - '
        end_index = i.find(end_symbol)
        s = i[start_index:end_index]
        s = datetime.strptime(s, '%Y-%m-%d %H:%M:%S.%f')
        date_from_file.append(s)

# распечатать эту дату, но на неделю позже. Должно получиться 2023-12-04 20:34:13.212967
one_week_delta = timedelta(weeks=1)
new_date = date_from_file[0] + one_week_delta
print(new_date.strftime('%Y-%m-%d %H:%M:%S.%f'))

# распечатать какой это будет день недели
day_of_week_name = date_from_file[1].strftime('%A')
print("День недели:", day_of_week_name)       

# распечатать сколько дней назад была эта дата
now = datetime.now()
days_before = now - date_from_file[2]
print("сколько дней назад была эта дата: ", days_before)
