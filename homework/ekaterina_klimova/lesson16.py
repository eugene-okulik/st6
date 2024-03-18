import random
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
    cursor = db.cursor()

    def create_new_group():
        cursor.execute("INSERT INTO `groups`(title) VALUES ('automation_db_python');")
        gr_id = cursor.lastrowid
        db.commit()
        return gr_id

    def create_new_student():
        cursor.execute("INSERT INTO students (name, second_name) VALUES ('Katerina', 'Klimova')")
        st_id = cursor.lastrowid
        db.commit()
        return st_id

    group_id = create_new_group()
    student_id = create_new_student()

    def student_in_group():
        cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))
        db.commit()

    student_in_group()

    def create_books():
        insert_books = "INSERT INTO books (title) VALUES (%s)"
        book = ["exorcist", "Elsewhere"]
        book_id = []
        for i in book:
            cursor.execute(insert_books, (i,))
            book_id.append(cursor.lastrowid)
        db.commit()
        return book_id

    books_id = create_books()

    def book_books():
        bk = "UPDATE books SET taken_by_student_id = %s WHERE id = %s;"
        for i in books_id:
            cursor.execute(bk, (student_id, i))
        db.commit()

    book_books()

    def create_subject():
        sub = "INSERT INTO subjets (title) VALUES (%s);"
        sub_vals = ["literature", "rhetoric"]
        sub_id = []
        for i in sub_vals:
            cursor.execute(sub, (i,))
            sub_id.append(cursor.lastrowid)
        db.commit()
        return sub_id

    subjects_id = create_subject()

    def create_lessons():
        lessons_id = []
        lessons = ["1_theme_l1", "2_theme_l1", "1_theme_l2", "2_theme_l2"]
        query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s);"
        for les, s_id in zip(lessons, subjects_id):
            cursor.execute(query, (les, s_id))
            lessons_id.append(cursor.lastrowid)
        db.commit()
        return lessons_id

    less_id = create_lessons()

    def create_marks():
        values = [random.randint(0, 100) for _ in range(4)]
        query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s);"
        for v, l_id in zip(values, less_id):
            cursor.execute(query, (v, l_id, student_id))
        db.commit()

    create_marks()

    queries = [
        """SELECT value FROM marks WHERE student_id = %s;""",
        """SELECT title FROM books WHERE taken_by_student_id = %s;""",
        """
        SELECT
            gr.title as group_name,
            s.name,
            s.second_name,
            b.title as book_title,
            sb.title as subject_name,
            l.title as lesson,
            m.value as mark
        FROM
            students s
            JOIN `groups` gr ON s.group_id = gr.id
            JOIN books b ON s.id =b.taken_by_student_id
            JOIN marks m ON m.student_id =s.id
            JOIN lessons l ON l.id  = m.lesson_id
            JOIN subjets sb ON sb.id = l.subject_id
        WHERE
            s.id = %s;
        """
    ]

    cursor.execute(queries[0], (student_id, ))
    marks = cursor.fetchall()

    cursor.execute(queries[1], (student_id,))
    books = cursor.fetchall()

    cursor.execute(queries[2], (student_id, ))
    st_info = cursor.fetchall()

    print("Marks of students: ", marks)
    print("Books of students: ", books)
    print("everything about students: ", st_info)
