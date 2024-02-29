import datetime


def date_conversion():
    try:
        user_date = input('Введите дату в формате (гггг/мм/дд): ')
        python_date = datetime.datetime.strptime(user_date, '%Y/%m/%d')
        return python_date
    except ValueError:
        return 'Неверный формат даты. Правильный формат даты: (гггг/мм/дд), например 2024/09/29'


print(date_conversion())
