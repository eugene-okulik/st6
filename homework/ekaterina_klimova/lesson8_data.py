import datetime

data = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(data, '%b %d, %Y - %X')
print("Распечатайте полное название месяца из этой даты:")
print(python_date.strftime('Month: %B'))

print("Распечатайте дату в таком формате: '15.01.2023, 12:05'")
print(python_date.strftime('%d.%m.%Y, %H:%M'))
