import mysql.connector as mysql

with mysql.connect(
        username='st6',
        password='AVNS_XGjY2YlfLXOaYWT4ZJU',
        host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
        port=25060,
        database='st6'
) as db:
    cursor = db.cursor(dictionary=True)
    cursor.execute("INSERT INTO students (name, second_name) VALUES ('Patrick', 'Star')")
    student_id = cursor.lastrowid
    db.commit()
    print(student_id)

    cursor.execute("UPDATE students SET group_id = 13 WHERE id = 89")
    db.commit()

    cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES "
                   "('Mathematics of Big Data', 89),"
                   "('The Deep Learning Revolution', 89), "
                   "('Designing an Internet', 89)")
    book_id = cursor.lastrowid
    db.commit()
    print(book_id)

    cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES "
                   "('Bikini Bottom', 14/03/2024, 17/04/2025)")
    group_id = cursor.lastrowid
    db.commit()
    print(group_id)

    cursor.execute("UPDATE `groups` SET start_date = '14/03/2024', end_date = '17/04/2025' WHERE id = 13")
    db.commit()

    cursor.execute("INSERT INTO subjets (title) VALUES"
                   "('Материаловедение'), "
                   "('Радиоэлектроника'), "
                   "('Схемотехника')")
    subject_id = cursor.lastrowid
    db.commit()
    print(subject_id)

    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES"
                   "('Виды диэдектриков', 18),"
                   "('Электроматериаловедение', 18),"
                   "('Радиоуправление летательными аппаратами', 19),"
                   "('Полупроводниковые приборы и электронные лампы', 19),"
                   "('Расчет радиаторов', 20),"
                   "('Вычислительные системы и микропроцессорная техника', 20)")
    lesson_id = cursor.lastrowid
    db.commit()
    print(lesson_id)

    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUE"
                   "('8', 36, 89),"
                   "('10', 37, 89),"
                   "('6', 38, 89),"
                   "('10', 39, 89),"
                   "('5', 40, 89),"
                   "('9', 41, 89)")
    mark_id = cursor.lastrowid
    db.commit()
    print(mark_id)

    cursor.execute('''
        SELECT name, second_name, value, title from students
        JOIN marks ON students.id = marks.student_id
        JOIN lessons ON lessons.id = marks.lesson_id
        WHERE student_id = 89
        ''')
    data = cursor.fetchall()
    print(data)
    for student in data:
        print(student['name'], student['value'], student['title'])

    cursor.execute("SELECT name, second_name, title FROM students "
                   "JOIN books ON students.id = books.taken_by_student_id "
                   "WHERE students.id = 89"
                   )
    data = cursor.fetchall()
    print(data)
    for books in data:
        print(books['name'], ':', books['title'])

    cursor.execute(
        "SELECT name, second_name, g.title as Title_group, b.title as Title_book, "
        "value, l.title as Title_lesson, s2.title as Title_subjets "
        "FROM students s "
        "JOIN `groups` g ON s.group_id = g.id "
        "JOIN books b ON s.id = b.taken_by_student_id "
        "JOIN marks m ON s.id = m.student_id "
        "JOIN lessons l ON l.id = m.lesson_id "
        "JOIN subjets s2 ON s2.id = l.subject_id "
        "WHERE s.id = 89"
        )
    data = cursor.fetchall()
    for i in data:
        print(i['name'], i['second_name'], i['Title_group'], i['Title_book'], i['value'], i['Title_lesson'],
              i['Title_subjets'], sep=': ')
