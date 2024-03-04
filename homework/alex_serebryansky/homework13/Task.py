import os
from datetime import timedelta, datetime

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'eugene_okulik', 'hw_13', 'data.txt')

with open(path, "r", encoding="utf-8") as file:
    data = file.read()


def parse_date(data_file: str) -> list:
    dates = []
    for string in data_file.splitlines():
        date = string.split(". ")
        dates.append(date[1].split(" -")[0])
    return dates


def get_date_after_week(date: str) -> str:
    return str(datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f") + timedelta(days=7))


def get_day_of_week(date: str) -> str:
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days_of_week[datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f").weekday()]


def get_days_ago(date: str) -> int:
    return (datetime.now() - datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")).days


print(get_date_after_week(parse_date(data)[0]))
print(get_day_of_week(parse_date(data)[1]))
print(get_days_ago(parse_date(data)[2]))
