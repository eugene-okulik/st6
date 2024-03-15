import mysql.connector as mysql
import os
import dotenv

dotenv.load_dotenv()

print(os.getenv('PORTDB'))
print(os.getenv('USERNAMEDB'))
print(os.getenv('PASSWORDDB'))
print(os.getenv('HOST'))
print(os.getenv('DATABASE'))

with mysql.connect(
    username=os.getenv('USERNAMEDB'),
    password=os.getenv('PASSWORDDB'),
    host=os.getenv('HOST'),
    port=os.getenv('PORTDB'),
    database=os.getenv('DATABASE'),
) as db:
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students LIMIT 2')
    data = cursor.fetchall()
    print(data)
