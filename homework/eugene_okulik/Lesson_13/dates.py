import datetime


now = datetime.datetime.now()
print(now)
today_midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
print(today_midnight)
after_midnight = now - today_midnight
print(after_midnight)
print(type(after_midnight))
ten_days = datetime.timedelta(days=10)
# ten_days_ago = now.replace(day=now.day-10)
ten_days_ago = now - ten_days
print(ten_days_ago)
