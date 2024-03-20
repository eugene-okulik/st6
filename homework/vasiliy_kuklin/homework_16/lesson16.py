import mysql.connector as mysql
import os

with mysql.connect(
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
) as db:
    cursor = db.cursor(dictionary=True)

    cursor.execute("INSERT INTO students(name, second_name) VALUES ('Мистер','Малой')")
    student_id = cursor.lastrowid

    cursor.execute(f"INSERT  INTO books (title, taken_by_student_id) values ('Гуси Лебеди',{student_id})")
    books_id = cursor.lastrowid

    cursor.execute("INSERT INTO `groups` (title) values ('Рэперы')")
    groups_id = cursor.lastrowid
    cursor.execute(f"UPDATE students  SET group_id  = {groups_id}")

    cursor.execute("INSERT INTO subjets (title) VALUES ('Пение')")
    first_subjects_id = cursor.lastrowid
    cursor.execute("INSERT INTO subjets (title) VALUES ('Рисование')")
    second_subjects_id = cursor.lastrowid

    # Создайте по два занятия для каждого предмета (lessons)
    cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Первое занятие', {first_subjects_id})")
    first_lesson_id = cursor.lastrowid

    cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Второе занятие', {first_subjects_id})")
    second_lesson_id = cursor.lastrowid

    cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Третье занятие', {second_subjects_id})")
    third_lesson_id = cursor.lastrowid

    cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Четвертое занятие', {second_subjects_id})")
    fourth_lesson_id = cursor.lastrowid

    # Поставьте своему студенту оценки (marks) для всех созданных вами занятий
    cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES (5, {first_lesson_id}, {student_id})")
    cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES (5, {second_lesson_id}, {student_id})")
    cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES (5, {third_lesson_id}, {student_id})")
    cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES (5, {fourth_lesson_id}, {student_id})")

# SELECTS
    # Все оценки студента
    cursor.execute(f"SELECT value FROM marks WHERE student_id = {student_id}")
    data = cursor.fetchall()
    print(data)

    # Все книги, которые находятся у студента
    cursor.execute(f"SELECT title FROM books WHERE taken_by_student_id = {student_id}")
    data = cursor.fetchall()
    print(data)

    query = f'''
    SELECT
    s.name as student, g.title as gruppa, b.title as kniga, m.value as ocenka,
    l.title as zanyatie, sb.title as predmet
    FROM students  s
    LEFT JOIN `groups` g
    ON s.group_id = g.id
    JOIN books b
    ON s.id = b.taken_by_student_id
    JOIN marks m
    ON s.id = m.student_id
    JOIN lessons l
    ON l.id = m.lesson_id
    JOIN subjets sb
    ON sb.id = l.subject_id
    WHERE s.id = {student_id}
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    db.commit()
