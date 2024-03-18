import mysql.connector as mysql
from homework.eugene_okulik.Lesson_16 import secrets

with mysql.connect(
    username=secrets.username,
    password=secrets.password,
    host=secrets.host,
    port=secrets.port,
    database=secrets.database,
) as db:
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students LIMIT 2')
    data = cursor.fetchall()
    print(data)
