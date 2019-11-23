from datetime import datetime
from Book import Book

class Library:
    def __init__(self,name,code):
        self.name = name
        self.sbn_code = code
        self.last_update = datetime.now()
        self.catalogue = []
        
    def add_book(self,book):
        self.catalogue.append(book)
        