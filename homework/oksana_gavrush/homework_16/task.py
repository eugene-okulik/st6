import mysql.connector as mysql
import os
import dotenv

dotenv.load_dotenv()

with mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
) as db:
    cursor = db.cursor(dictionary=True)
    student_name = 'Lion'
    student_second_name = 'King'
    cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)",
                   (student_name, student_second_name))

    student_id = cursor.lastrowid
    db.commit()

    insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
    cursor.executemany(insert_query, [('Event studies', student_id), ('Tourism and Gastronomy', student_id)])
    db.commit()

    cursor.execute("INSERT INTO `groups` (title) VALUES ('Greenpeace')")
    grouping_id = cursor.lastrowid
    db.commit()

    cursor.execute("UPDATE students SET group_id = %s WHERE name = %s AND second_name = %s",
                   (grouping_id, student_name, student_second_name))
    db.commit()

    insert_query_item = "INSERT INTO subjets (title) VALUES (%s)"
    subjects = [('Religious tourism',), ('Foreign tourism',)]
    subjects_id = []
    for subject in subjects:
        cursor.execute(insert_query_item, subject)
        subjects_id.append(cursor.lastrowid)
    db.commit()

    insert_query_lesson = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
    lessons_data = [
        ('Marketing in tourism', subjects_id[0]),
        ('Tourism: regulatory legal acts', subjects_id[0]),
        ('Tourism and Gastronomy', subjects_id[1]),
        ('Cultural Tourism', subjects_id[1])
    ]

    insert_lesson_ids = []
    for lesson in lessons_data:
        cursor.execute(insert_query_lesson, lesson)
        insert_lesson_ids.append(cursor.lastrowid)
    db.commit()

    insert_query_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
    cursor.executemany(insert_query_marks, [
        (5, insert_lesson_ids[0], student_id),
        (4, insert_lesson_ids[1], student_id),
        (5, insert_lesson_ids[2], student_id),
        (5, insert_lesson_ids[3], student_id)])
    db.commit()

    cursor.execute("SELECT students.name, students.second_name, "
                   "marks.value FROM marks "
                   "JOIN students ON marks.student_id = students.id "
                   "WHERE students.id = %s", (student_id,))

    data = cursor.fetchall()
    school_grades = []
    for grades in data:
        school_grades.append(int(grades['value']))
    print(f"Student's school grades: {school_grades}")

    cursor.execute("SELECT books.title "
                   "FROM books "
                   "JOIN students ON books.taken_by_student_id = students.id "
                   "WHERE students.id = %s", (student_id,))

    find_book = cursor.fetchall()
    school_books = []
    for book in find_book:
        school_books.append(book['title'])
    print(f"Student books: {school_books}")

    cursor.execute("SELECT students.name, students.second_name, groups.title  AS group_title, "
                   "lessons.title AS lesson, subjets.title AS subjets, marks.value AS grade "
                   "FROM students "
                   "JOIN `groups` on students.group_id = `groups`.id "
                   "JOIN marks on marks.student_id = students.id "
                   "JOIN lessons on lessons.id = marks.lesson_id "
                   "JOIN subjets on subjets.id = lessons.subject_id "
                   "WHERE students.id = %s", (student_id,))
    all_information = cursor.fetchall()
    for info in all_information:
        print(info)
