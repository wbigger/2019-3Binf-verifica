from datetime import datetime 
from Book import Book

class Library :
    def __init__ (self,name,code):
        self.name = name
        self.sbn_code = code
        self.last_update = datetime.now() 
        self.catalogue = []

    def add_book (self,book):
        self.catalogue.append(book)

marconi = Library("Biblioteca IIS Marconi","CIVMA")

harry_potter = Book("Harry Potter qualcosa","JKR","Salani",1997,350,12345)

marconi.add_book(harry_potter)

print(marconi.name)
print(marconi.sbn_code)
print(marconi.last_update)
print(marconi.catalogue)