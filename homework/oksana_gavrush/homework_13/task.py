import os
from datetime import datetime, timedelta

repo_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
patch_fail = os.path.join(repo_path, 'eugene_okulik', 'hw_13', 'data.txt')
with open(patch_fail, 'r', encoding='utf-8') as file:
    data = file.read()

blocks = data.split('\n')
list_data = []
for section in blocks:
    split_my_srt = section.split('. ', 1)
    rest_of_string = split_my_srt[1]
    date_description = rest_of_string.split(' - ')
    list_data.append(date_description[0])

week_more = list_data[0]
date_format = '%Y-%m-%d %H:%M:%S.%f'
initial_date = datetime.strptime(week_more, date_format)
new_date = initial_date + timedelta(days=7)
new_date_string = new_date.strftime(date_format)
print(new_date_string)

find_day_weekend = list_data[1]
initial_date = datetime.strptime(find_day_weekend, date_format)
day_of_week_number = initial_date.weekday()
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(days_of_week[day_of_week_number - 1])

how_many_days_ago = list_data[2]
current_date = datetime.now()
date_format = '%Y-%m-%d %H:%M:%S.%f'
initial_date = datetime.strptime(how_many_days_ago, date_format)
days_difference = (current_date - initial_date).days
print(days_difference)
