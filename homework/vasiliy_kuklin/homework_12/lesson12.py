# Исключения
import datetime

my_data = input("Введите дату (в таком виде 2023/06/05 12 hours, 30 mins, 10 secs): ")


def format_data():
    try:
        python_date = datetime.datetime.strptime(my_data, '%Y/%m/%d %H hours, %M mins, %S secs')
        print(python_date)
    # except (ZeroDivisionError, TypeError) as err:
    except ValueError:
        # return print('some where')
        print("Вы ввели не верный формат даты")
        return print(("Введите дату (в таком виде 2023/06/05 12 hours, 30 mins, 10 secs)"))


input_data = format_data()
