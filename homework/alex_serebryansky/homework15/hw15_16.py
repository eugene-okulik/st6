import mysql.connector as mysql
import os
import dotenv


class Mark:
    EXCELLENT = 5
    GOOD = 4
    NOT_BAD = 3
    BAD = 2
    DONT_GIVE_UP = 1
    STUPID = 0


dotenv.load_dotenv()

with mysql.connect(
        username=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSW'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME')
) as db:
    cursor = db.cursor(dictionary=True)

    cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('T-99', '25/03/2024', '24/05/2024')")
    group_id = cursor.lastrowid
    db.commit()

    cursor.execute("INSERT INTO students (name, second_name, group_id)"
                   "VALUES ('Tester', 'Testovich', %s)", (group_id,))
    student_id = cursor.lastrowid
    db.commit()

    books_title = ['How increase to senior QA', 'How increase to Tech led of QA']
    books_ids = []
    for book in books_title:
        cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
                       (book, student_id,))
        books_ids.append(cursor.lastrowid)
        db.commit()

    subjects = ['Example_1', 'Example_2']
    subjects_ids = []
    for subject in subjects:
        cursor.execute("INSERT INTO subjets (title) VALUES (%s)", (subject,))
        subjects_ids.append(cursor.lastrowid)
        db.commit()

    lesson_titles = [('For exemple_1_1', subjects_ids[0]),
                     ('For exemple_1_2', subjects_ids[0]),
                     ('For exemple_2_1', subjects_ids[1]),
                     ('For exemple_2_2', subjects_ids[1])
                     ]
    lessons_ids = []
    for lesson in lesson_titles:
        cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", lesson)
        lessons_ids.append(cursor.lastrowid)
        db.commit()

    cursor.executemany("INSERT INTO marks (value, lesson_id, student_id) VALUE (%s, %s, %s)",
                       [
                           (Mark.DONT_GIVE_UP, lessons_ids[0], student_id),
                           (Mark.NOT_BAD, lessons_ids[1], student_id),
                           (Mark.EXCELLENT, lessons_ids[2], student_id),
                           (Mark.GOOD, lessons_ids[3], student_id)
                       ])
    db.commit()
    student_id = 154
    cursor.execute("SELECT m.value, s.name, s.second_name "
                   "FROM marks m JOIN students s ON s.id = m.student_id "
                   "WHERE m.student_id = %s", (student_id,))
    data = cursor.fetchall()
    for item in data:
        print(f"Student {item['name']} has {item['value']} mark")

    cursor.execute("SELECT b.title, s.name, s.second_name FROM books b "
                   "JOIN students s on s.id = b.taken_by_student_id "
                   "WHERE s.id = %s", (student_id,))
    data = cursor.fetchall()
    for item in data:
        print(f"Student {item['name']} has book: {item['title']}")

    cursor.execute("SELECT g.title as 'number_of_group', b.title as 'taken_books', s.name, s.second_name, "
                   "sub.title as 'subject', l.title as 'lesson', m.value as 'mark' FROM `groups` g "
                   "JOIN students s on g.id = s.group_id "
                   "JOIN books b on s.id = b.taken_by_student_id "
                   "JOIN marks m on s.id = m.student_id "
                   "JOIN lessons l on l.id = m.lesson_id "
                   "JOIN subjets sub on sub.id = l.subject_id "
                   "WHERE s.id = %s", (student_id,))
    data = cursor.fetchall()
    for item in data:
        print(item['name'], item['second_name'], item['number_of_group'], item['subject'], item['lesson'], item['mark'])
