from datetime import datetime
from Book import Book

class Library:
    def __init__(self, name, sbn_code):
        self.name = name
        self.sbn_code = sbn_code
        self.last_update = datetime.now()
        self.catalogue = []

    def add_book(self,Book):
        self.catalogue.append(Book)

marconi = Library("BIBLIOTECA IIS Marconi", "CIVMA")
harry_potter = Book("Harry Potter e la pietra filosofale","J. K. Rowling","Salani Editore",1997, 294, 8877827025)

assert marconi.name == "BIBLIOTECA IIS Marconi"
assert marconi.sbn_code == "8877827025"
assert marconi.last_update == ""
assert len(marconi.catalogue) == "0"

marconi.add_book(harry_potter)

assert len(marconi.catalogue) == "1"
