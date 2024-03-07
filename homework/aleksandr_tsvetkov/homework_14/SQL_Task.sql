INSERT INTO students (name, second_name) VALUES ('Aleksandr', 'Tsvetkov');

UPDATE students SET group_id = 5 WHERE id = 3;

INSERT INTO books (title, taken_by_student_id) VALUES
('Talent on Demand', 3),
('Data Science for Business', 3),
('The Signal and the Noise', 3);

INSERT INTO `groups` (title) VALUES ('Mathematical');

UPDATE students SET group_id = 7 WHERE id = 3;

INSERT INTO subjets (title) VALUES
('Геометрия'), ('Иностранный язык'), ('Философия');

INSERT INTO lessons (title, subject_id) VALUES
('Геометрические фигуры', 8), ('Векторы', 8),
('Программа по английскому языку "Дневник путешественника"', 9), ('формирование лексических навыков по теме', 9),
('Ионийская философия', 10), ('Пифагор и пифагорейцы', 10);

INSERT INTO marks (value, lesson_id, student_id) VALUES
('4', 16, 3), ('5', 17, 3), (5, 18, 3), (5, 19,3), (3, 20, 3), (3, 21, 3);

SELECT name, second_name, value, title from students
JOIN marks ON students.id = marks.student_id 
JOIN lessons ON lessons.id = marks.lesson_id
WHERE student_id = 3;

SELECT name, second_name,  title FROM students
JOIN books ON students.id = books.taken_by_student_id
WHERE taken_by_student_id = 3;

SELECT name, second_name, g.title as Title_group, b.title as Title_book, 
value, l.title as Title_lesson, s2.title as Title_subjets
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets s2 ON s2.id = l.subject_id
WHERE s.id = 3;
