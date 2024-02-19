from homework.alex_serebryansky.homework10.Book import Book


class SchoolBook(Book):

    def __init__(self, title: str, author: str, pages: int, subject: str,
                 class_number: str, isbn=None, is_reserved=False, availability_of_tasks=True):
        super().__init__(title, author, pages, isbn, is_reserved)
        self.subject = subject
        self.class_number = class_number
        self.availability_of_tasks = availability_of_tasks

    def book_print(self):
        if self.is_reserved is True:
            print(f'The title is: {self.title}, author: {self.author}, number of page: {self.pages}, '
                  f'subject: {self.subject}, school class: {self.class_number} <RESERVED>')
        else:
            print(f'The title is: {self.title}, author: {self.author}, number of page: {self.pages}, '
                  f'subject: {self.subject}, school class: {self.class_number}')
