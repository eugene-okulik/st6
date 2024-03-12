INSERT INTO st6.students (name, second_name) VALUES(69, 'Nick', 'Dazenov');
INSERT INTO st6.students (name, second_name) VALUES(71, 'Boris', 'Zylo')

INSERT INTO st6.books (title, taken_by_student_id) VALUES('Социология', 69);
INSERT INTO st6.books (title, taken_by_student_id) VALUES('Алгоритмы', 69);
INSERT INTO st6.books (title, taken_by_student_id) VALUES('A Practitioners Guide to Software Test Design', 71);

INSERT INTO st6.`groups` (title) VALUES('Гуманитарии');

UPDATE st6.students SET group_id=5 WHERE id=71;
UPDATE st6.students SET group_id=1 WHERE id=69;

INSERT INTO st6.subjets (title) VALUES('Программирование');
INSERT INTO st6.subjets (title) VALUES('Физика');
INSERT INTO st6.subjets (title) VALUES('Основы алгоритмизации');
INSERT INTO st6.subjets (title) VALUES('Теоретическая механика');
INSERT INTO st6.subjets (title) VALUES('Аналитическая алгебра');

INSERT INTO st6.lessons (title, subject_id) VALUES('Вводное занятие', 2);
INSERT INTO st6.lessons (title, subject_id) VALUES('Вводное занятие', 1);
INSERT INTO st6.lessons (title, subject_id) VALUES('Вводное занятие', 3);
INSERT INTO st6.lessons (title, subject_id) VALUES('Вводное занятие', 4);
INSERT INTO st6.lessons (title, subject_id) VALUES('Вводное занятие', 5);

INSERT INTO st6.lessons (title, subject_id) VALUES('Лекция о классах', 1);
INSERT INTO st6.lessons (title, subject_id) VALUES('Строение вещества. Молекулы и атомы', 2);
INSERT INTO st6.lessons (title, subject_id) VALUES('Формульно-словесный способ описания алгоритма', 3);
INSERT INTO st6.lessons (title, subject_id) VALUES('Введение в раздел «Кинематика»', 4);
INSERT INTO st6.lessons (title, subject_id) VALUES( 'Извлечение корня из комплексного числа', 5);

INSERT INTO st6.marks (value, lesson_id, student_id) VALUES('5', 1, 69);
INSERT INTO st6.marks (value, lesson_id, student_id) VALUES('4', 2, 69);
INSERT INTO st6.marks (value, lesson_id, student_id) VALUES('5', 3, 69);
INSERT INTO st6.marks (value, lesson_id, student_id) VALUES('3', 4, 69);
INSERT INTO st6.marks (value, lesson_id, student_id) VALUES('5', 5, 69);
INSERT INTO st6.marks (value, lesson_id, student_id) VALUES('4', 6, 69);
INSERT INTO st6.marks (value, lesson_id, student_id) VALUES('5', 7, 69);
INSERT INTO st6.marks (value, lesson_id, student_id) VALUES('5', 8, 69);
INSERT INTO st6.marks (value, lesson_id, student_id) VALUES('3', 9, 69);
INSERT INTO st6.marks (value, lesson_id, student_id) VALUES('4', 10, 69);

SELECT s.name, s.second_name , m.value from students s join marks m on s.id = m.student_id WHERE s.id=69

SELECT s.name, s.second_name , b.title as book_title  from students s join books b on s.id = b.taken_by_student_id  WHERE s.id=69

SELECT distinct * from students s 
join marks m on s.id = m.student_id
join `groups` g on s.group_id  = g.id
join lessons l on m.lesson_id =l.id 
join subjets s2  on l.subject_id =s2.id 
join books b on s.id = b.taken_by_student_id
WHERE s.id=69
