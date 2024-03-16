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
    cursor.execute("INSERT INTO students (name, second_name) VALUES ('Jack', 'Jonson')")
    student_id = cursor.lastrowid
    db.commit()
    print(student_id)

    # Заполнение таблицы 'books'
    insert_query_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
    books = [('Mathematics of Big Data', student_id),
             ('The Deep Learning Revolution', student_id),
             ('Designing an Internet', student_id)]
    books_id = []
    for book in books:
        cursor.execute(insert_query_books, book)
        books_id.append(cursor.lastrowid)
        db.commit()

    # Заполнение таблицы 'groups'
    cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES "
                   "('The Transporter', '17/03/2024', '18/04/2025')")
    group_id = cursor.lastrowid
    db.commit()
    print(group_id)

    cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id,))
    db.commit()

    # Заполнение таблицы 'subjets'
    insert_query_subjects = "INSERT INTO subjets (title) VALUES (%s)"
    subjects = [('Делопроизводство',), ('Инвестиции',)]
    subjects_id = []
    for subject in subjects:
        cursor.execute(insert_query_subjects, subject)
        subjects_id.append(cursor.lastrowid)
        db.commit()
    print(subjects_id)

    # Заполнение таблицы 'lessons'
    insert_query_lessons = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
    lessons = [('анализ инвестиционных проектов', subjects_id[0]),
               ('Зависимость инвестиций', subjects_id[0]),
               ('Оценка инвестиционного климата', subjects_id[1]),
               ('Финансовое обеспечение инвестиционных проектов', subjects_id[1])]
    lessons_id = []
    for lesson in lessons:
        cursor.execute(insert_query_lessons, lesson)
        lessons_id.append(cursor.lastrowid)
        db.commit()
    print(lessons_id)

    # Заполнение таблицы 'marks
    insert_query_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUE (%s, %s, %s)"
    cursor.executemany(insert_query_marks, [
        (8, lessons_id[0], student_id),
        (10, lessons_id[1], student_id),
        (6, lessons_id[2], student_id),
        (10, lessons_id[3], student_id)])
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
                   "WHERE students.id = %s", (student_id,))
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
