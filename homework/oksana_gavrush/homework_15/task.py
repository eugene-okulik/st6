import mysql.connector as mysql

with mysql.connect(
    user='st6',
    passwd='AVNS_XGjY2YlfLXOaYWT4ZJU',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st6'
) as db:
    cursor = db.cursor(dictionary=True)

    def insert_into():
        cursor.execute("INSERT INTO students (name, second_name) VALUES ('Lion', 'King')")
        db.commit()

    def append_books():
        insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
        cursor.executemany(insert_query, [('Felix Salten Bambi', 80), ('Discovery', 80)])
        db.commit()

    def append_groups():
        cursor.execute("INSERT INTO `groups` (title) VALUES ('Greenpeace')")
        db.commit()

    def group_for_students():
        cursor.execute("UPDATE students SET group_id=12 WHERE name='Lion' AND second_name ='King'")
        db.commit()

    def append_item():
        insert_query_item = "INSERT INTO subjets (title) VALUES (%s)"
        cursor.executemany(insert_query_item, [('Ecology',), ('Natural Sciences',)])
        db.commit()

    def append_lessons():
        insert_query_lesson = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
        cursor.executemany(insert_query_lesson, [
            ('Methods for studying nature', 16),
            ('Populations', 16),
            ('Ecology concepts', 17),
            ('Studying biology', 17)])
        db.commit()

    def append_marks():
        insert_query_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
        cursor.executemany(insert_query_marks, [
            (5, 32, 80),
            (4, 33, 80),
            (5, 34, 80),
            (5, 35, 80)])
    db.commit()

    cursor.execute("SELECT students.name, students.second_name, "
                   "marks.value FROM marks "
                   "JOIN students ON marks.student_id = students.id "
                   "WHERE students.name = 'Lion'")
    data = cursor.fetchall()
    school_grades = []
    for grades in data:
        school_grades.append(int(grades['value']))
    print(f"Student's school grades: {school_grades}")

    cursor.execute("SELECT books.title "
                   "FROM books "
                   "JOIN students ON books.taken_by_student_id = students.id "
                   "WHERE students.name = 'Lion'")
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
                   "WHERE students.name = 'Lion'")
    all_information = cursor.fetchall()
    for info in all_information:
        print(info)
