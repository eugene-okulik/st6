import datetime


def date_conversion():
    while True:
        try:
            user_date = input('Введите дату: ')
            python_date = datetime.datetime.strptime(user_date, '%d.%m.%Y')
            return f'Питоновский формат даты: {python_date}'
        except ValueError:
            print('Неверный формат даты. Правильный формат даты: (дд/мм/гггг), например 29.09.2024')


print(date_conversion())
