import mysql.connector
import os
import dotenv


dotenv.load_dotenv()

db_connect = mysql.connector.connect(
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
)


with db_connect as db:
    my_cursor = db.cursor(dictionary=True)

    my_cursor.execute("INSERT INTO students (name, second_name) VALUES ('TestName', 'TestSecondName')")
    student_id = my_cursor.lastrowid
    db.commit()

    my_cursor.execute("INSERT INTO st6.`groups` (title) VALUES ('TestGroup99')")
    group_id = my_cursor.lastrowid
    db.commit()

    update_group_req = 'UPDATE students SET group_id=%s WHERE id=%s'
    my_cursor.execute(update_group_req, (group_id, student_id))
    db.commit()

    my_cursor.execute("INSERT INTO subjets (title) VALUES ('Math_test')")
    subject_id = my_cursor.lastrowid
    db.commit()

    insert_lesson_req = "INSERT INTO lessons (title, subject_id) VALUES ('Lesson_test_title', %s)"
    my_cursor.execute(insert_lesson_req, (subject_id,))
    lesson_id = my_cursor.lastrowid
    db.commit()

    insert_marks_req = """
    INSERT INTO st6.marks (value, lesson_id, student_id)
    VALUES(666,%s,%s)
    """
    my_cursor.execute(insert_marks_req, (lesson_id, student_id))
    db.commit()

    select_student_marks_req = """
    SELECT m.value, l.title
    from students s
    join marks m on s.id = m.student_id
    join lessons l on m.lesson_id = l.id
    WHERE s.id=%s
    """
    my_cursor.execute(select_student_marks_req, (student_id,))
    print(my_cursor.fetchall())
    print('******')

    insert_book_req = "INSERT INTO books (title, taken_by_student_id) VALUES ('Book_test', %s)"
    my_cursor.execute(insert_book_req, (student_id,))
    book_id = my_cursor.lastrowid
    db.commit()

    select_student_books_req = """
    SELECT s.name, s.second_name , b.title as book_title
    FROM students s
    join books b on s.id = b.taken_by_student_id
    WHERE s.id=%s
    """
    my_cursor.execute(select_student_books_req, (student_id,))
    student_books = my_cursor.fetchall()
    print(student_books)
    print('******')

    select_student_all_req = """
    SELECT * from students s
    join marks m on s.id = m.student_id
    join `groups` g on s.group_id  = g.id
    join lessons l on m.lesson_id =l.id
    join subjets s2  on l.subject_id =s2.id
    join books b on s.id = b.taken_by_student_id
    WHERE s.id=%s
    """
    my_cursor.execute(select_student_all_req, (student_id,))
    info_student = my_cursor.fetchall()
    print(info_student)
    print('******')
