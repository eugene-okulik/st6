INSERT INTO st6.students (id, name, second_name) VALUES(69, 'Nick', 'Dazenov');
INSERT INTO st6.students (id, name, second_name) VALUES(71, 'Boris', 'Zylo')

INSERT INTO st6.books (id, title, taken_by_student_id) VALUES(4, 'Социология', 69);
INSERT INTO st6.books (id, title, taken_by_student_id) VALUES(3, 'Алгоритмы', 69);
INSERT INTO st6.books (id, title, taken_by_student_id) VALUES(34, 'A Practitioners Guide to Software Test Design', 71);

INSERT INTO st6.`groups` (id, title) VALUES(5, 'Гуманитарии');

UPDATE st6.students SET group_id=5 WHERE id=71;
UPDATE st6.students SET group_id=1 WHERE id=69;

INSERT INTO st6.subjets (id, title) VALUES(1, 'Программирование');
INSERT INTO st6.subjets (id, title) VALUES(2, 'Физика');
INSERT INTO st6.subjets (id, title) VALUES(3, 'Основы алгоритмизации');
INSERT INTO st6.subjets (id, title) VALUES(4, 'Теоретическая механика');
INSERT INTO st6.subjets (id, title) VALUES(5, 'Аналитическая алгебра');

INSERT INTO st6.lessons (id, title, subject_id) VALUES(1, 'Вводное занятие', 2);
INSERT INTO st6.lessons (id, title, subject_id) VALUES(2, 'Вводное занятие', 1);
INSERT INTO st6.lessons (id, title, subject_id) VALUES(3, 'Вводное занятие', 3);
INSERT INTO st6.lessons (id, title, subject_id) VALUES(4, 'Вводное занятие', 4);
INSERT INTO st6.lessons (id, title, subject_id) VALUES(5, 'Вводное занятие', 5);

INSERT INTO st6.lessons (id, title, subject_id) VALUES(6, 'Лекция о классах', 1);
INSERT INTO st6.lessons (id, title, subject_id) VALUES(7, 'Строение вещества. Молекулы и атомы', 2);
INSERT INTO st6.lessons (id, title, subject_id) VALUES(8, 'Формульно-словесный способ описания алгоритма', 3);
INSERT INTO st6.lessons (id, title, subject_id) VALUES(9, 'Введение в раздел «Кинематика»', 4);
INSERT INTO st6.lessons (id, title, subject_id) VALUES(10, 'Извлечение корня из комплексного числа', 5);

INSERT INTO st6.marks (id, value, lesson_id, student_id) VALUES(1, '5', 1, 69);
INSERT INTO st6.marks (id, value, lesson_id, student_id) VALUES(2, '4', 2, 69);
INSERT INTO st6.marks (id, value, lesson_id, student_id) VALUES(3, '5', 3, 69);
INSERT INTO st6.marks (id, value, lesson_id, student_id) VALUES(4, '3', 4, 69);
INSERT INTO st6.marks (id, value, lesson_id, student_id) VALUES(5, '5', 5, 69);
INSERT INTO st6.marks (id, value, lesson_id, student_id) VALUES(6, '4', 6, 69);
INSERT INTO st6.marks (id, value, lesson_id, student_id) VALUES(7, '5', 7, 69);
INSERT INTO st6.marks (id, value, lesson_id, student_id) VALUES(8, '5', 8, 69);
INSERT INTO st6.marks (id, value, lesson_id, student_id) VALUES(9, '3', 9, 69);
INSERT INTO st6.marks (id, value, lesson_id, student_id) VALUES(10, '4', 10, 69);
