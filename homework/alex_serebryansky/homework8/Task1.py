import datetime

date = 'Jan 15, 2023 - 12:05:33'
parse_date = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')
print(parse_date.strftime('%B'))
print(parse_date.strftime('%d.%m.%Y, %H:%M'))
