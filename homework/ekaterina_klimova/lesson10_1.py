class Book:
    def __init__(self, title, author, pages, ISBN="isbn", mat="бумага", isText="Да", isBooked=False):
        self.mat = mat
        self.isText = isText
        self.title = title
        self.author = author
        self.pages = pages
        self.ISBN = ISBN
        self.isBooked = isBooked


def print_info(b):
    if book.isBooked:
        res_status = "зарезервирована"
    else:
        res_status = ""
    print(f'Название: {b.title}, Автор: {b.author}, Количество страниц: {b.pages}, Материал: {b.mat}, {res_status}')


book1 = Book("Идиот", "Ф.М.Достоевский", 500, isBooked=True)
book2 = Book("Ася", "И.С.Тургеньев", 680)
book3 = Book("Анна Каренина", "Л.Н.Толстой", 400)
book4 = Book("Мцыри", "М.Ю.Лермонтов", 300)
book5 = Book("Человек, который смеется", "В.М.Гюго", 450)

print_info(book1)
print_info(book2)
print_info(book3)
print_info(book4)
print_info(book5)
