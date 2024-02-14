import datetime

init_date = 'Jan 15, 2023 - 12:05:33'
py_date = datetime.datetime.strptime(init_date, '%b %d, %Y - %H:%M:%S')
month = py_date.strftime('%B')
print(py_date)
print(month)

req_date_format = py_date.strftime('%d.%m.%Y, %H:%M')
print(req_date_format)
