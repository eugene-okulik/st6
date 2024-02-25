class Book:
    def __init__(self, title, author, numberOfPages, ISBN = "isbn", matherial = "бумага", isText = "Да", isBooked = False):
        self.matherial = matherial
        self.isText = isText
        self.title = title
        self.author = author
        self.numberOfPages = numberOfPages
        self.ISBN = ISBN
        self.isBooked = isBooked


def print_info(book):
    if book.isBooked:
        reserved_status = "зарезервирована"
    else:
        reserved_status = ""
    print(f'Название: {book.title}, Автор: {book.author}, Количество страниц: {book.numberOfPages}, Материал: {book.matherial},
           {reserved_status}')


book1 = Book("Идиот", "Ф.М.Достоевский", 500, isBooked = True)
book2 = Book("Ася", "И.С.Тургеньев", 680)
book3 = Book("Анна Каренина", "Л.Н.Толстой", 400)
book4 = Book("Мцыри", "М.Ю.Лермонтов", 300)
book5 = Book("Человек, который смеется", "В.М.Гюго", 450)

print_info(book1)
print_info(book2)
print_info(book3)
print_info(book4)
print_info(book5)
