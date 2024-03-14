import mysql.connector as mysql

with mysql.connect(
        username='st6',
        password='AVNS_XGjY2YlfLXOaYWT4ZJU',
        host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
        port=25060,
        database='st6'
) as db:
    cursor = db.cursor(dictionary=True)

    # Заполнение таблицы 'students'
    cursor.execute("INSERT INTO students (name, second_name) VALUES ('Patrick', 'Star')")
    student_id = cursor.lastrowid
    db.commit()
    print(student_id)

    # Заполнение таблицы 'books'
    cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES "
                   "('Mathematics of Big Data', 89),"
                   "('The Deep Learning Revolution', 89), "
                   "('Designing an Internet', 89)")
    book_id = cursor.lastrowid
    db.commit()
    print(book_id)

    # # Заполнение таблицы 'groups'
    cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES "
                   "('Bikini Bottom', 14/03/2024, 17/04/2025)")
    group_id = cursor.lastrowid
    db.commit()
    print(group_id)

    cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id,))
    db.commit()

    cursor.execute("UPDATE `groups` SET start_date = '14/03/2024', end_date = '17/04/2025' WHERE id = %s",
                   (group_id,))
    db.commit()

    # # Заполнение таблицы 'subjets'
    cursor.execute("INSERT INTO subjets (title) VALUES"
                   "('Материаловедение'), "
                   "('Радиоэлектроника'), "
                   "('Схемотехника')")
    subject_id = cursor.lastrowid
    db.commit()
    print(subject_id)

    # # Заполнение таблицы 'lessons'
    insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
    cursor.executemany(insert_query, [
        ('Виды диэдектриков', subject_id),
        ('Электроматериаловедение', subject_id),
        ('Радиоуправление летательными аппаратами', subject_id),
        ('Полупроводниковые приборы и электронные лампы', subject_id),
        ('Расчет радиаторов', subject_id),
        ('Вычислительные системы и микропроцессорная техника', subject_id)
    ])
    lesson_id = cursor.lastrowid
    db.commit()

    # # Заполнение таблицы 'marks
    insert_query_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUE (%s, %s, %s)"
    cursor.executemany(insert_query, [
        ('8', lesson_id, student_id),
        ('10', lesson_id, student_id),
        ('6', lesson_id, student_id),
        ('10', lesson_id, student_id),
        ('5', lesson_id, student_id),
        ('9', lesson_id, student_id)
    ])
    mark_id = cursor.lastrowid
    db.commit()

# Все оценки студента.
    cursor.execute(
        "SELECT name, second_name, value, title from students "
        "JOIN marks ON students.id = marks.student_id "
        "JOIN lessons ON lessons.id = marks.lesson_id "
        "WHERE student_id = %s", (student_id,))
    data = cursor.fetchall()
    print(data)
    for student in data:
        print(student['name'], student['value'], student['title'])

# Все книги, которые находятся у студента
    cursor.execute("SELECT name, second_name, title FROM students "
                   "JOIN books ON students.id = books.taken_by_student_id "
                   "WHERE students.id = %s", (student_id,)
                   )
    data = cursor.fetchall()
    print(data)
    for books in data:
        print(books['name'], ':', books['title'])

# Все о студенте
    cursor.execute(
        "SELECT name, second_name, g.title as Title_group, b.title as Title_book, "
        "value, l.title as Title_lesson, s2.title as Title_subjets "
        "FROM students s "
        "JOIN `groups` g ON s.group_id = g.id "
        "JOIN books b ON s.id = b.taken_by_student_id "
        "JOIN marks m ON s.id = m.student_id "
        "JOIN lessons l ON l.id = m.lesson_id "
        "JOIN subjets s2 ON s2.id = l.subject_id "
        "WHERE s.id = %s", (student_id,)
    )
    data = cursor.fetchall()
    for i in data:
        print(i['name'], i['second_name'], i['Title_group'], i['Title_book'], i['value'], i['Title_lesson'],
              i['Title_subjets'], sep=': ')
