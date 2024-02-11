import datetime

# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:
# 1. Распечатайте полное название месяца из этой даты
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"


date1 = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(date1, '%b %d, %Y - %H:%M:%S')
print(python_date)
print(python_date.strftime('%B'))
print(python_date.strftime('%d.%m.%Y, %H:%M'))
