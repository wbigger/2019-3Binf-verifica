from datetime import datetime 
from book import book
class Library:

    def __init__(self, name, code):
        self.name = name
        self.sbn_code = code
        self.last_update = datetime.now()
        self.catalogue = []

    def add_book(self, book):
        self.catalogue.append(book)    

Marconi = Library("IIS Marconi","CIVMA")    
harry_potter = Book("harry pottere e la pietra dsa", "J.K.Zozzing", "Salami editore", 1984, 174, 5768439)     

print(Marconi.name)
print(Marconi.sbn_code)
print(Marconi.last_update)
print(Marconi.catalogue)

