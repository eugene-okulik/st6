-- Создайте студента (student)
INSERT INTO students(name, second_name) VALUES ('Ioan','Grozny')

-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT  INTO books (title, taken_by_student_id)
VALUES ('Kniga_odin', (SELECT id FROM students WHERE name = 'Ioan' AND second_name = 'Grozny'))

INSERT  INTO books (title, taken_by_student_id)
VALUES ('Kniga_dva', (SELECT id FROM students WHERE name = 'Ioan' AND second_name = 'Grozny'))

INSERT  INTO books (title, taken_by_student_id)
VALUES ('Kniga_tri', (SELECT id FROM students WHERE name = 'Ioan' AND second_name = 'Grozny'))

-- Создайте группу (group) и определите своего студента туда
INSERT INTO `groups` (title) values ('Aria')

UPDATE students  SET group_id  = (SELECT id FROM `groups` WHERE title = 'Aria' ) WHERE name = 'Ioan' AND second_name = 'Grozny'

-- Создайте несколько учебных предметов (subjects)
INSERT INTO subjets (title) VALUES ('Histori_Russia')

INSERT INTO subjets (title) VALUES ('Geographi_Russia')

-- Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons (title, subject_id) VALUES ('Zanyatie 1', (SELECT id FROM subjets WHERE title = 'Histori_Russia'))

INSERT INTO lessons (title, subject_id) VALUES ('Zanyatie 2', (SELECT id FROM subjets WHERE title = 'Histori_Russia'))

INSERT INTO lessons (title, subject_id) VALUES ('Zanyatie 1', (SELECT id FROM subjets WHERE title = 'Geographi_Russia'))

INSERT INTO lessons (title, subject_id) VALUES ('Zanyatie 2', (SELECT id FROM subjets WHERE title = 'Geographi_Russia'))

-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий

INSERT INTO marks (value, lesson_id, student_id)
VALUES (5,
(SELECT id FROM lessons WHERE title = 'Zanyatie 1' AND subject_id = (SELECT id FROM subjets WHERE title = 'Histori_Russia')),
(SELECT id FROM students WHERE name = 'Ioan' AND second_name = 'Grozny'))

INSERT INTO marks (value, lesson_id, student_id)
VALUES (5,
(SELECT id FROM lessons WHERE title = 'Zanyatie 2' AND subject_id = (SELECT id FROM subjets WHERE title = 'Histori_Russia')),
(SELECT id FROM students WHERE name = 'Ioan' AND second_name = 'Grozny'))

INSERT INTO marks (value, lesson_id, student_id)
VALUES (5,
(SELECT id FROM lessons WHERE title = 'Zanyatie 1' AND subject_id = (SELECT id FROM subjets WHERE title = 'Geographi_Russia')),
(SELECT id FROM students WHERE name = 'Ioan' AND second_name = 'Grozny'))

INSERT INTO marks (value, lesson_id, student_id)
VALUES (5,
(SELECT id FROM lessons WHERE title = 'Zanyatie 2' AND subject_id = (SELECT id FROM subjets WHERE title = 'Geographi_Russia')),
(SELECT id FROM students WHERE name = 'Ioan' AND second_name = 'Grozny'))

-- Получите информацию из базы данных:
-- Все оценки студента
    SELECT value FROM marks WHERE student_id = (SELECT id FROM students WHERE name = 'Ioan' AND second_name = 'Grozny')

-- Все книги, которые находятся у студента
    SELECT title FROM books WHERE taken_by_student_id = (SELECT id FROM students WHERE name = 'Ioan' AND second_name = 'Grozny')

-- Для вашего студента выведите всё, что о нем есть в базе:
-- группа, книги, оценки с названиями занятий и предметов
-- (всё одним запросом с использованием Join)
SELECT s.name as student, g.title as gruppa, b.title as kniga, m.value as ocenka, l.title as zanyatie, sb.title as predmet
FROM students  s
LEFT JOIN `groups` g
ON s.group_id =g.id
JOIN books b
ON s.id = b.taken_by_student_id
JOIN marks m
ON s.id = m.student_id
JOIN lessons l
ON l.id = m.lesson_id
JOIN subjets sb
ON sb.id = l.subject_id
WHERE s.name = 'Ioan'
AND s.second_name = 'Grozny'
