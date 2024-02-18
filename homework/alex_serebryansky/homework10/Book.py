class Book:
    page_material = 'paper'
    presence_of_text = True

    def __init__(self, title: str, author: str, pages: int, isbn=None, is_reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = is_reserved

    def book_print(self):
        if self.is_reserved is True:
            print(f'The title is: {self.title}, author: {self.author}, number of page: {self.pages}, '
                  f'material of page: {self.page_material} <RESERVED>')
        else:
            print(f'The title is: {self.title}, author: {self.author}, number of page: {self.pages}, '
                  f'material of page: {self.page_material}')
