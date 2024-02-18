class Book:
    def __init__(self, name, author, number_of_pages, is_reserved=False):
        self.name = name
        self.author = author
        self.number_of_pages = number_of_pages
        self.is_reserved = is_reserved

    book_material = 'бумага'
    has_text = True
    ISBN = ''

    def reservation(self):
        if self.is_reserved != False:
            print('зарезервирована')
        return ''

    def book_print(self, material=book_material):
        print((f'Название: {self.name}, Автор: {self.author}, страниц: {self.number_of_pages}, материал: {material}'))
        print(self.reservation())


class Books_school(Book):
    def __init__(self, subject, author, number_of_pages, school_class, name='', has_tasks=False, is_reserved=False):
        super().__init__(name, author, number_of_pages, is_reserved)
        self.subject = subject
        self.school_class = school_class
        self.has_tasks = has_tasks

    def school_book_print(self):
        print(f'Предмет: {self.subject}, Автор: {self.author}, страниц: {self.number_of_pages}, класс: {self.school_class}')
        print(self.reservation())


book1 = Book('Идиот', 'Достоевский', 500)
book1.book_print()

book2 = Book('Преступление и наказание', 'Достоевский', 300, True)
book2.book_print()

book3 = Book(name='Звезды и полосы', author='Гаррисон', number_of_pages=480)
book3.is_reserved = True
book3.book_print()

school_book1 = Books_school(subject='Алгебра', number_of_pages=115, author='Иванов', school_class='8Б')
school_book1.school_book_print()

school_book2 = Books_school('География', 89, 'Круглов', '7А')
school_book2.is_reserved = True
school_book2.school_book_print()

school_book3 = Books_school('История', 666, 'Вековой', '6В', is_reserved=True)
school_book3.school_book_print()
