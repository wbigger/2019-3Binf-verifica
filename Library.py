from datetime import datetime
from Book import Book

class Library:
    def __init__(self, name, sbn_code):
        self.name = name
        self.sbn_code = sbn_code
        self.last_update = datetime.now()
        self.catalogue = []

    def add_book(self,book):
        self.catalogue.append(book)

marconi = Library("BIBLIOTECA IIS Marconi", "CIVMA")
harry_potter = book("Harry Potter e la pietra filosofale","J. K. Rowling","Salani Editore",1997, 294, 8877827025)
marconi.add_book(harry_potter)

print(marconi.name)
print(marconi.sbn_code)
print(marconi.last_update)
print(marconi.catalogue)