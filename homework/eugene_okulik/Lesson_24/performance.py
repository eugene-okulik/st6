import requests
from datetime import datetime


before = datetime.now()
requests.get('https://jsonplaceholder.typicode.com/posts')
after = datetime.now()
time_elapsed = after - before
print(time_elapsed)
