class Book:
    page_material = 'paper'
    text_presence = 'Yes'

    def __init__(self, book_title, author, pages_count, isbn, reserved=False):
        self.reserved = reserved
        self.isbn = isbn
        self.pages_count = pages_count
        self.author = author
        self.book_title = book_title

    def reserve(self):
        reserved_status = ': *** RESERVED! ***' if self.reserved is True else ''
        print(f'Title: {self.book_title}, Author: {self.author}, '
              f'Pages: {self.pages_count}, Material: {self.page_material}{reserved_status}')


class SchoolBooks(Book):
    def __init__(self, book_title, author, pages_count, isbn, subject, school_class, tasks=False, reserved=False):
        super().__init__(book_title, author, pages_count, isbn, reserved)
        self.tasks = tasks
        self.school_class = school_class
        self.subject = subject

    def reserve(self):
        reserved_status = ': *** RESERVED! ***' if self.reserved is True else ''
        print(f'Title: {self.book_title}, author: {self.author}, pages: {self.pages_count}, '
              f'subject: {self.subject}, school_class: {self.school_class}{reserved_status}')


book1 = Book('Идиот', 'Достоевский', 500, 92959)
book2 = Book('Мастер и Маргарита', 'Михаил Булгаков', 300, 49492)
book3 = Book('Собачье сердце', 'Михаил Булгаков', 400, 149194)
book4 = Book('Преступление и наказание', 'Федор Достоевский', 356, 194914)
book5 = Book('Мертвые души', 'Николай Гоголь', 223, 14919490, reserved=True)
book1.reserve(), book2.reserve(), book3.reserve(), book4.reserve(), book5.reserve()


math_book = SchoolBooks('Алгебра', 'Аванг Сариян', '258', '1481480',
                        'Математика', 7)
history_book = SchoolBooks('История Беларуси', 'Астахова Лариса', '157', '1481480',
                           'История', 6)
geography_book = SchoolBooks('География', 'Вальцов Николай', '189', '1481480',
                             'География', 9)
physics_book = SchoolBooks('Физика', 'Виленкин Наум', '89', '1481480',
                           'Физика', 10, reserved=True)
math_book.reserve(), history_book.reserve(), geography_book.reserve(), physics_book.reserve()
