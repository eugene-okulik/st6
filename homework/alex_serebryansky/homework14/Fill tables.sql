INSERT INTO `groups` (title, start_date, end_date) VALUES ('T-66', '04/02/2024', '24/05/2024');

INSERT INTO students (name, second_name, group_id) VALUES ('Py', 'Thon', (SELECT id FROM `groups` WHERE title = 'T-66'));

INSERT INTO books (title, taken_by_student_id) VALUES ('Python basic', (SELECT id FROM students WHERE name = 'Py' AND second_name = 'Thon'));
INSERT INTO books (title, taken_by_student_id) VALUES ('SQL basic', (SELECT id FROM students WHERE name = 'Py' AND second_name = 'Thon'));

INSERT INTO subjets (title) VALUES ('Programming');
INSERT INTO subjets (title) VALUES ('Theory of testing');
INSERT INTO subjets (title) VALUES ('Science of computer');

INSERT INTO lessons (title, subject_id) VALUES ('Programming lesson 1', (SELECT id FROM subjets WHERE title='Programming'));
INSERT INTO lessons (title, subject_id) VALUES ('Programming lesson 2', (SELECT id FROM subjets WHERE title='Programming'));
INSERT INTO lessons (title, subject_id) VALUES ('ToT lesson 1', (SELECT id FROM subjets WHERE title='Theory of testing'));
INSERT INTO lessons (title, subject_id) VALUES ('ToT lesson 2', (SELECT id FROM subjets WHERE title='Theory of testing'));
INSERT INTO lessons (title, subject_id) VALUES ('SoC lesson 1', (SELECT id FROM subjets WHERE title='Science of computer'));
INSERT INTO lessons (title, subject_id) VALUES ('SoC lesson 2', (SELECT id FROM subjets WHERE title='Science of computer'));

INSERT INTO marks (value, lesson_id, student_id)
VALUES ('Perfect',
        (SELECT id FROM lessons WHERE title = 'Programming lesson 1'),
        (SELECT id FROM students WHERE name = 'Py' AND second_name = 'Thon'));

INSERT INTO marks (value, lesson_id, student_id)
VALUES ('Perfect',
        (SELECT id FROM lessons WHERE title = 'Programming lesson 2'),
        (SELECT id FROM students WHERE name = 'Py' AND second_name = 'Thon'));

INSERT INTO marks (value, lesson_id, student_id)
VALUES ('Perfect',
        (SELECT id FROM lessons WHERE title = 'ToT lesson 1'),
        (SELECT id FROM students WHERE name = 'Py' AND second_name = 'Thon'));

INSERT INTO marks (value, lesson_id, student_id)
VALUES ('Perfect',
        (SELECT id FROM lessons WHERE title = 'ToT lesson 2'),
        (SELECT id FROM students WHERE name = 'Py' AND second_name = 'Thon'));

INSERT INTO marks (value, lesson_id, student_id)
VALUES ('Perfect',
        (SELECT id FROM lessons WHERE title = 'SoC lesson 1'),
        (SELECT id FROM students WHERE name = 'Py' AND second_name = 'Thon'));

INSERT INTO marks (value, lesson_id, student_id)
VALUES ('Perfect',
        (SELECT id FROM lessons WHERE title = 'SoC lesson 2'),
        (SELECT id FROM students WHERE name = 'Py' AND second_name = 'Thon'));