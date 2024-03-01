class Book:
    mat = "бумага"
    isText = True

    def __init__(self, title, author, pages, ISBN="isbn", isBooked=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.ISBN = ISBN
        self.isBooked = isBooked


def print_info(b):
    if b.isBooked:
        res_status = "зарезервирована"
    else:
        res_status = ""
    print(f'Название: {b.title}, Автор: {b.author}, '
          f'Количество страниц: {b.pages}, '
          f'Материал: {b.mat}, {res_status}')


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


class SchoolBook(Book):
    def __init__(self, subject, grade, title, author, pages, ISBN="isbn", mat="бумага",
                 isText="Да", isBooked=False, task=True):
        super().__init__(title, author, pages, ISBN, mat, isText, isBooked)
        self.subject = subject
        self.grade = grade
        self.task = task


book6 = SchoolBook("Алгебра", 9, "Математика", "Иванов", 500, isBooked=True)
book7 = SchoolBook("География", 9, "География", "Сидоров", 300)


def print_info(sB):
    if sB.isBooked:
        res_status = "зарезервирована"
    else:
        res_status = ""
    print(f'Название: {sB.title}, Автор: {sB.author}, '
          f'Количество страниц: {sB.pages}, '
          f'Материал: {sB.mat}, {res_status}')


print_info(book6)
print_info(book7)
