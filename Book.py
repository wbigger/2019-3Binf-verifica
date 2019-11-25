import re

class Book:
    def __init__(self,title,author,publisher,year, pages, book_id):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        print("hello")
        self.isbn = book_id if self.is_isbn_valid(book_id) else None
        self.sbn_code = book_id if self.is_sbn_code_valid(book_id) else None
        self.is_bulky = self.pages > 500
        
    def is_valuable(self, current_year):
        return current_year - self.year > 20 or current_year - self.year < 1
    
    def is_isbn_valid(self,isbn):
        idx = 1
        accumulator = 0
        isbn_base = str(isbn)[:-1]

        if isbn_base.isdigit() == False:
            return False

        isbn_check = int(str(isbn)[-1:])

        for i in isbn_base:
            accumulator += int(i) * idx
            idx +=1
        accumulator = accumulator % 11
        return accumulator == isbn_check

    def is_sbn_code_valid(self,code):
        print(f"code is {code}")
        if not isinstance(code, str):
            print(f"code not a string")
            return False
        return re.search("^[A-Z]{2}\\\\[A-Z]{4}\\\\[A-Z0-9]{3}\\\\[0-9]{7}", code) != None

    def has_isbn(self):
        return self.isbn != None

    def has_sbn_code(self):
        return self.sbn_code != None
