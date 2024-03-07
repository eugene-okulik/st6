SELECT m.value, s.name, s.second_name FROM marks m
JOIN students s on s.id = m.student_id
WHERE s.name = 'Py';

SELECT b.title, s.name, s.second_name FROM books b
JOIN students s on s.id = b.taken_by_student_id
WHERE s.name = 'Py';

SELECT g.title as 'number_of_group', b.title as 'taken_books', s.name, s.second_name,
       sub.title as 'subject', l.title as 'lesson', m.value as 'mark' FROM `groups` g
JOIN students s on g.id = s.group_id
JOIN books b on s.id = b.taken_by_student_id
JOIN marks m on s.id = m.student_id
JOIN lessons l on l.id = m.lesson_id
JOIN subjets sub on sub.id = l.subject_id
WHERE s.name = 'Py';