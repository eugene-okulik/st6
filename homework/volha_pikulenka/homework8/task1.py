import datetime

init_date = 'Jan 15, 2023 - 12:05:33'
py_date = datetime.datetime.strptime(init_date, '%b %d, %Y - %H:%M:%S')
print(py_date)

req_date_format = py_date.strftime('%d.%m.%Y, %H:%M')
print(req_date_format)
