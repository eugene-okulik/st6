import datetime

init_date = 'Jan 15, 2023 - 12:05:33'
date_in_py = datetime.datetime.strptime(init_date, '%b %d, %Y - %H:%M:%S')
print(datetime.datetime.strptime(init_date, '%b %d, %Y - %H:%M:%S'))

req_format = date_in_py.strftime('%d.%m.%Y, %H:%M')
print(req_format)
