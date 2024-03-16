-- Создайте студента (student)
INSERT INTO students(name, second_name) VALUES ('Mark','Twen')

-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT  INTO books (title, taken_by_student_id) values ('Skazki', 121)

INSERT  INTO books (title, taken_by_student_id) values ('Shutki', 121)

INSERT  INTO books (title, taken_by_student_id) values ('Pribautki', 121)

-- Создайте группу (group) и определите своего студента туда
INSERT INTO `groups` (title) values ('Aria')

UPDATE students  SET group_id  = (SELECT id FROM `groups` WHERE title = 'Aria' ) WHERE name = 'Mark'

-- Создайте несколько учебных предметов (subjects)
INSERT INTO subjets (title) VALUES ('Geodezika')

INSERT INTO subjets (title) VALUES ('Arganaftika')

-- Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons (title, subject_id) VALUES ('Zanyatie one', (SELECT id FROM subjets WHERE title = 'Geodezika'))

INSERT INTO lessons (title, subject_id) VALUES ('Zanyatie two', (SELECT id FROM subjets WHERE title = 'Geodezika'))

INSERT INTO lessons (title, subject_id) VALUES ('Zanyatie one', (SELECT id FROM subjets WHERE title = 'Arganaftika'))

INSERT INTO lessons (title, subject_id) VALUES ('Zanyatie two', (SELECT id FROM subjets WHERE title = 'Arganaftika'))

-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий

INSERT INTO marks (value, lesson_id, student_id)
VALUES (5,
(SELECT id FROM lessons WHERE title = 'Zanyatie one' AND subject_id = (SELECT id FROM subjets WHERE title = 'Geodezika')),
(SELECT id FROM students WHERE name = 'Mark'))

INSERT INTO marks (value, lesson_id, student_id)
VALUES (5,
(SELECT id FROM lessons WHERE title = 'Zanyatie two' AND subject_id = (SELECT id FROM subjets WHERE title = 'Geodezika')),
(SELECT id FROM students WHERE name = 'Mark'))

INSERT INTO marks (value, lesson_id, student_id)
VALUES (5,
(SELECT id FROM lessons WHERE title = 'Zanyatie one' AND subject_id = (SELECT id FROM subjets WHERE title = 'Arganaftika')),
(SELECT id FROM students WHERE name = 'Mark'))

INSERT INTO marks (value, lesson_id, student_id)
VALUES (5,
(SELECT id FROM lessons WHERE title = 'Zanyatie two' AND subject_id = (SELECT id FROM subjets WHERE title = 'Arganaftika')),
(SELECT id FROM students WHERE name = 'Mark'))
