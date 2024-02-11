import datetime

# Обработка даты
data = "Jan 15, 2023 - 12:05:33"
pythone_date = datetime.datetime.strptime(data, '%b %d, %Y - %I:%M:%S')
my_month = datetime.datetime.strftime(pythone_date, '%B')
print(pythone_date)
print(my_month)

# "15.01.2023, 12:05"
new_format_data = datetime.datetime.strftime(pythone_date, '%d.%m.%Y, %I:%M')
print(new_format_data)

# Map, filter
temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
    34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
    29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

new_list_temperatues = list(filter(lambda x: x >= 28, temperatures))
print(f'Новый список (1 вариант): {new_list_temperatues}')

max_temperatures = list(map(lambda x: x, filter(lambda x: x >= 28, temperatures)))
print(f'Новый список (2 вариант): {max_temperatures}')
print(f'Максималььная тепература: {max(max_temperatures)}')
print(f'Минимальная тепература: {min(max_temperatures)}')
print(f'Средняя тепература: {sum(max_temperatures)/len(max_temperatures)}')
