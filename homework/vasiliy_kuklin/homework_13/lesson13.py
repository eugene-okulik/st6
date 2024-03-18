import os
import datetime

my_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

path_to_file = os.path.join(my_path, 'st6', 'homework', 'eugene_okulik', 'hw_13', 'data.txt')

with open(path_to_file, 'r', encoding='utf-8') as open_file:
    my_data = open_file.read()

features = {}
elements = my_data.splitlines()
days_week = {
    0: 'Понедельник',
    1: 'Вторник',
    2: 'Среда',
    3: 'Четверг',
    4: 'Пятница',
    5: 'Суббота',
    6: 'Воскресенье'
}

for element in elements:
    if element.startswith('1. '):
        print(element)
        element_data = element[3:29]
        python_date = datetime.datetime.strptime(element_data, '%Y-%m-%d %H:%M:%S.%f')
        new_python_date = python_date + datetime.timedelta(weeks=1)
        print(f'Новая дата на неделю больше: {new_python_date}')
    elif element.startswith('2. '):
        print(element)
        element_data = element[3:29]
        python_date = datetime.datetime.strptime(element_data, '%Y-%m-%d %H:%M:%S.%f')
        day_of_weeks = python_date.isoweekday()
        print(f'День недели {days_week.get(day_of_weeks)}')
    elif element.startswith('3. '):
        print(element)
        element_data = element[3:29]
        python_date = datetime.datetime.strptime(element_data, '%Y-%m-%d %H:%M:%S.%f')
        day_now = datetime.datetime.now()
        print(day_now)
        print(f'Столько дней назад: {(python_date - day_now).days}')
