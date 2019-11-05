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
    

marconi = Library("IIS Marconi Library", "CIVMA")
print("The name of the library is: " + marconi.name)
print("The sbn code of the library is: " + marconi.sbn_code)
       
harry_potter = Book("Harry Potter e la Pietra Filosofale", "J.K Rownling", "Salani Editore", 1997, 294, 990239089128 )
marconi.add_book(harry_potter)