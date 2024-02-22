# Библиотека
# Первый класс
class Book:
    page_material = 'бумага'
    presence_of_text = True

    def __init__(self, book_title, author, number_of_pages, ISBN, reserved):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.reserved = reserved

    def details_book(self):
        if self.reserved:
            print(
                f'Название: {self.book_title}, '
                f'Автор: {self.author}, '
                f'страниц: {self.number_of_pages}, '
                f'материал: {self.page_material}, '
                f'зарезервирована'
            )
        elif not self.reserved:
            print(
                f'Название: {self.book_title}, '
                f'Автор: {self.author}, '
                f'страниц: {self.number_of_pages}, '
                f'материал: {self.page_material}'
            )


dostoevsky_idiot = Book('Идиот', 'Достоевсикй', 500, 123, True)
print(dostoevsky_idiot.details_book())

dostoevsky_idiot_not_reserved = Book('Идиот', 'Достоевсикй', 500, 123, False)
print(dostoevsky_idiot_not_reserved.details_book())

pushkin_skazki = Book('Сказки', 'Пушкин', 600, 124, True)
print(pushkin_skazki.details_book())

esenin_stihi = Book('Стихи', 'Есенин', 300, 125, True)
print(esenin_stihi.details_book())

fantastic = Book('Фантастика', 'Народные', 3900, 126, False)
print(fantastic.details_book())


# Второй класс
class School_Book(Book):

    def __init__(self, book_title, author, number_of_pages, ISBN, reserved, predmet, klazz, zadanie):
        super().__init__(book_title, author, number_of_pages, ISBN, reserved)
        self.predmet = predmet
        self.klazz = klazz
        self.zadanie = zadanie

    def detali_school_book(self):
        if self.reserved:
            print(
                f'Название: {self.book_title}, '
                f'Автор: {self.author}, '
                f'страниц: {self.number_of_pages}, '
                f'предмет: {self.predmet}, '
                f'класс: {self.klazz}, '
                f'зарезервирована'
            )
        elif not self.reserved:
            print(
                f'Название: {self.book_title}, '
                f'Автор: {self.author}, '
                f'страниц: {self.number_of_pages}, '
                f'предмет: {self.predmet}, '
                f'класс: {self.klazz}, '
            )


mathematic = School_Book('Алгебра', 'Иванов', 200, 100, True, 'Математика', 9, None)
print(mathematic.detali_school_book())
geometry = School_Book('Геометрия', 'Петров', 201, 101, False, 'Геометрия', 10, None)
print(geometry.detali_school_book())

biology = School_Book('Биология', 'Проживальский', 102, 104, False, 'Ботаника', 4, None)
print(biology.detali_school_book())
