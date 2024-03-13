import mysql.connector as mysql

with mysql.connect(
    username='st6',
    password='AVNS_XGjY2YlfLXOaYWT4ZJU',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st6',
) as db:
    cursor = db.cursor(dictionary=True)

    def first_select():
        cursor.execute('SELECT * FROM students')
        data = cursor.fetchall()
        print(data)
        for student in data:
            print(student['second_name'])

    def get_one():
        cursor.execute('SELECT * FROM students WHERE id = 6')
        # cursor.execute('SELECT * FROM `groups` ORDER BY end_date DESC LIMIT 1')
        data = cursor.fetchone()
        print(data)
        print(data['second_name'])

    def insert_into():
        cursor.execute("INSERT INTO students (name, second_name) VALUES ('Bob', 'Sponge')")
        student_id = cursor.lastrowid
        db.commit()
        print(student_id)

    def incorrect_formatting():
        login = input('login')
        passw = input('passw')
        cursor.execute(f"SELECT * FROM students WHERE name = '{login}' and second_name='{passw}'")
        user = cursor.fetchone()
        if user:
            print('you are logged in')


    def correct_formatting():
        login = input('login')
        passw = input('passw')
        select_request = "SELECT * FROM students WHERE name = %s and second_name= %s"
        cursor.execute(select_request, (login, passw))
        user = cursor.fetchone()
        if user:
            print('you are logged in')

    insert_query = "INSERT INTO books (title) VALUES (%s)"
    cursor.execute(insert_query, ('Как я провел свое лето',))
    book1 = cursor.lastrowid
    # cursor.executemany(
    #     insert_query,
    #     [('Tom Sawer',), ('War and peace',)]
    # )
    # book2 = cursor.lastrowid
    books = [('Tom Sawer',), ('War and peace',)]
    book_ids = []
    for book in books:
        cursor.execute(insert_query, book)
        book_ids.append(cursor.lastrowid)
    db.commit()
    print(book1, book_ids)

query = '''
SELECT s.name, g.title as group_title, b.title as book_title  
FROM students s
RIGHT JOIN `groups` g
on s.group_id = g.id 
join books b
on s.id = b.taken_by_student_id 
WHERE s.name = 'Aex'
'''
