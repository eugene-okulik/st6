import os
import datetime


path_to_repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
path_to_file = os.path.join(path_to_repo, 'homework', 'eugene_okulik', 'hw_13', 'data.txt')

with open(path_to_file, 'r', encoding='UTF-8') as open_file:
    data = open_file.read()

date = []
for line in data.split('\n'):  # делим на строки, используя разделитель новой строки
    number, dates, time, *action = line.split()  # разбиваем на элементы
    date.append(datetime.datetime.strptime(f'{dates} {time}', '%Y-%m-%d %H:%M:%S.%f'))

print(date[0] + datetime.timedelta(weeks=1))  # распечатать эту дату, но на неделю позже
print(date[1].strftime("%A"))  # распечатать какой это будет день недели
print(datetime.datetime.now() - date[2])  # распечатать сколько дней назад была эта дата
