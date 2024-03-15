import mysql.connector

def prettify(func):
    def wrapper(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('********')
    return wrapper


db_connect = mysql.connector.connect(
    username='st6',
    password='AVNS_XGjY2YlfLXOaYWT4ZJU',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st6',
)

with db_connect as db:
    mycursor = db.cursor(dictionary=True)

    @prettify
    def print_databases():
        mycursor.execute("SHOW DATABASES")
        for dbs in mycursor:
            print(dbs)

    @prettify
    def insert_student_and_print(name, second_name):
        insert_req = "INSERT INTO students (name, second_name) VALUES (%s, %s);"
        mycursor.execute(insert_req, (name, second_name))
        id = mycursor.lastrowid
        select_req = "Select * FROM students where id = %s"
        mycursor.execute(select_req, (id,))
        student = mycursor.fetchone()
        db.commit()
        print(f'Successfully dded {student}')

    @prettify
    def update_student_group_id(group_id, id):
        update_req = "UPDATE students SET group_id=%s WHERE id=%s"
        mycursor.execute(update_req, (group_id, id))
        db.commit()
        select_req = "Select * FROM students WHERE id=%s"
        mycursor.execute(select_req, (id,))
        student = mycursor.fetchone()
        print(f'Updated record: {student}')

    @prettify
    def insert_subject(subj_title):
        insert_req = "INSERT INTO subjets (title) VALUES (%s)"
        mycursor.execute(insert_req, (subj_title,))
        id = mycursor.lastrowid
        select_req = "Select * FROM subjets WHERE id=%s"
        mycursor.execute(select_req, (id,))
        subj = mycursor.fetchone()
        db.commit()
        print(f'Added subject is: {subj}')

    @prettify
    def insert_lessons(lesson_title, subject_id):
        insert_req = "INSERT INTO lessons (title, subject_id) VALUES (%s,%s)"
        mycursor.execute(insert_req, (lesson_title, subject_id))
        db.commit()
        select_req = "Select * FROM lessons WHERE title=%s"
        mycursor.execute(select_req, (lesson_title,))
        lesson = mycursor.fetchone()
        print(f'Added subject is: {lesson}')

    @prettify
    def insert_students_marks(value, lesson_id, student_id):
        insert_req = """
        INSERT INTO st6.marks (value, lesson_id, student_id)
        VALUES(%s,%s,%s)
        """
        mycursor.execute(insert_req, (value, lesson_id, student_id))
        db.commit()
        select_req = """
        SELECT s.name, s.second_name , m.value, l.title 
        from students s 
        join marks 
        m on s.id = m.student_id 
        join lessons l 
        on m.lesson_id = l.id 
        WHERE s.id=%s
        """
        mycursor.execute(select_req, (student_id,))
        print(f'Students marks: {mycursor.fetchall()}')

    @prettify
    def select_students_marks(student_id):
        select_req = """
        SELECT m.value, l.title
        from students s
        join marks m on s.id = m.student_id
        join lessons l on m.lesson_id = l.id
        WHERE s.id=%s
        """
        mycursor.execute(select_req, (student_id,))
        print(mycursor.fetchall())

    @prettify
    def select_students_books(student_id):
        select_req = """
        SELECT s.name, s.second_name , b.title as book_title
        FROM students s
        join books b on s.id = b.taken_by_student_id
        WHERE s.id=%s
        """
        mycursor.execute(select_req, (student_id,))
        print(mycursor.fetchall())

    @prettify
    def select_student_all_info(student_id):
        select_req = """
        SELECT * from students s
        join marks m on s.id = m.student_id
        join `groups` g on s.group_id  = g.id
        join lessons l on m.lesson_id =l.id
        join subjets s2  on l.subject_id =s2.id
        join books b on s.id = b.taken_by_student_id
        WHERE s.id=%s
        """
        mycursor.execute(select_req, (student_id,))
        result = mycursor.fetchall()
        if result:
            print(result)
        else:
            print("No student with such id")

    @prettify
    def insert_book_and_print(title):
        insert_req = "INSERT INTO books (title) VALUES (%s)"
        select_req = "Select * FROM books where id = %s"
        mycursor.execute(insert_req, (title,))
        id = mycursor.lastrowid
        mycursor.execute(select_req, (id,))
        book = mycursor.fetchone()
        db.commit()

        print(f"You added book '{book}'")

    # print_databases()
    # select_student_all_info(69)
    # insert_book_and_print('test  book')
    # insert_books_and_print()
    # insert_student_and_print('Peter', 'Longbottom')
    # update_student_group_id(10, 69)
    # insert_subject('AQA')
    # insert_lessons('new class', 15)
    # insert_students_marks(100, 9, 69)
    # select_students_marks(69)
    # select_students_books(69)
