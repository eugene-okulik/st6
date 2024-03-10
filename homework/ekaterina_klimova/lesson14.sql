INSERT INTO groups (title) VALUES ('automation');

INSERT INTO students (name, second_name) VALUES ('Kate', 'Klimova')

UPDATE students SET group_id = 11
WHERE id = 76; 

INSERT INTO books (title) VALUES ('The Pragmatic Programmer');
INSERT INTO books (title) VALUES ('Advanced Security Tester Syllabus');

UPDATE books SET taken_by_student_id = 76 
WHERE id IN (43, 44);

INSERT INTO subjets (title) VALUES ('phylosophy');
INSERT INTO subjets (title) VALUES ('forensics');

INSERT INTO lessons (title, subject_id) VALUES ('1_philosophy of ancient india', 14);
INSERT INTO lessons (title, subject_id) VALUES ('2_philosophy and worldview', 14);
INSERT INTO lessons (title, subject_id) VALUES ('1_criminal thinking', 15);
INSERT INTO lessons (title, subject_id) VALUES ('2_Identification feature', 15);

INSERT INTO marks (value, lesson_id, student_id) VALUES (10, 28, 76);
INSERT INTO marks (value, lesson_id, student_id) VALUES (9, 29, 76);
INSERT INTO marks (value, lesson_id, student_id) VALUES (10, 30, 76);
INSERT INTO marks (value, lesson_id, student_id) VALUES (8, 31, 76);

SELECT value FROM marks
WHERE student_id = 76

SELECT title FROM books
WHERE taken_by_student_id = 76

SELECT gr.title as group_name, 
s.name, 
s.second_name,
b.title as book_title,
sb.title as subject_name,
l.title as lesson,
m.value as mark
FROM students s 
JOIN `groups` gr ON s.group_id = gr.id 
JOIN books b ON s.id =b.taken_by_student_id
JOIN marks m ON m.student_id =s.id
JOIN lessons l ON l.id  = m.lesson_id 
JOIN subjets sb ON sb.id = l.subject_id
WHERE s.id = 76;