from datetime import datetime
from Book import Book

class Library:
    def __init__(self, name, code):
        self.name = name
        self.sbn_code = code
        self.last_update = datetime.now()
        self.catalogue = []
    
    def add_book(self,book):
        self.catalogue.append(book)
        self.last_update = datetime.now()

    def add_books(self,books):
        self.catalogue += books
        self.last_update = datetime.now()
