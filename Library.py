from datetime import datetime
from Book import Book
class Library:
    def __init__(self, name, sbn_code):
        self.name = name
        self.sbn_code = sbn_code
        self.last_update = datetime.now()
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)
    


