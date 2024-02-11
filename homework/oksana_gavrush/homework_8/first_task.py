from datetime import datetime


date_string = 'Jan 15, 2023 - 12:05:33'

datetime_object = datetime.strptime(date_string, '%b %d, %Y - %H:%M:%S')

month_name = datetime_object.strftime("%B")
print(month_name)

formatted_date_time = datetime_object.strftime("%d.%m.%Y, %H:%M")
print(formatted_date_time)
