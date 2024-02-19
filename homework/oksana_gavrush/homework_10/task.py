class Book:
    page_material = 'endpaper'
    language_of_text = 'English'
    book_reserved = False

    def __init__(self, book_title, author, number_of_pages, isbn):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn

    def __str__(self):
        if self.book_reserved:
            return (f'Book title: {self.book_title}, Author: {self.author}, pages: {self.number_of_pages},'
                    + f' material: {self.page_material}, reserved')
        else:
            return (f'Book title: {self.book_title}, Author:{self.author}, pages:{self.number_of_pages},'
                    + f' material: {self.page_material}')


class SchoolBook(Book):

    def __init__(self, subject, class_number, has_exercises=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subject = subject
        self.class_number = class_number
        self.has_exercises = has_exercises

    def __str__(self):
        if self.book_reserved:
            return (f'Book title: {self.book_title}, Author: {self.author}, pages: {self.number_of_pages}, '
                    + f'subject: {self.subject}, school class: {self.class_number}, reserved')
        else:
            return (f'Book title: {self.book_title}, Author: {self.author}, pages: {self.number_of_pages}, '
                    + f'subject: {self.subject} school class: {self.class_number}')


book_1 = Book(book_title='Towards Swan', author='Marcel Proust', number_of_pages=1221, isbn='979-10-90636-07-1')
book_1.book_reserved = True
book_2 = Book(book_title='Sodom and Gomorrah', author='Marcel Proust', number_of_pages=981, isbn='979-30-90336-07-2')
book_3 = Book(book_title='Discipline', author='Jocko Willing', number_of_pages=1381, isbn='179-30-90336-07-3')
book_4 = Book(book_title='World Order', author='Henry JKissinger', number_of_pages=2381, isbn='179-10-90346-07-3')
book_5 = Book(book_title='Peaceful Warrior', author='Dan Mailman', number_of_pages=3381, isbn='179-30-30336-07-5')
print(book_1, book_2, book_3, book_4, book_5, sep='\n')
print()

school_book_1 = SchoolBook(book_title='Algebra', author='Arefieva Irina', number_of_pages=320,
                           isbn='979-10-90636-08-1', subject='mathematics', class_number=7)
school_book_1.book_reserved = True
school_book_2 = SchoolBook(book_title='Geometry', author='Alla Ershova', number_of_pages=410,
                           isbn='979-10-90636-07-2', subject='mathematics', class_number=10)
print(school_book_1, school_book_2, sep='\n')
