from homework.alex_serebryansky.homework10.Book import Book
from homework.alex_serebryansky.homework10.SchoolBook import SchoolBook

total_list = [
    Book('Idiot', 'Dostoevsky', 500),
    Book('Idiot', 'Dostoevsky', 500, is_reserved=True),
    Book('Idiot', 'Dostoevsky', 500),
    Book('Idiot', 'Dostoevsky', 500, is_reserved=True),
    Book('Idiot', 'Dostoevsky', 500),
    SchoolBook('Algebra', 'Ivanov', 200, 'Mathematics', '9', is_reserved=True),
    SchoolBook('Algebra', 'Ivanov', 200, 'Mathematics', '9'),
    SchoolBook('Algebra', 'Ivanov', 200, 'Mathematics', '9', is_reserved=True),
    SchoolBook('Algebra', 'Ivanov', 200, 'Mathematics', '9'),
    SchoolBook('Algebra', 'Ivanov', 200, 'Mathematics', '9', is_reserved=True)
]

[book.book_print() for book in total_list]
