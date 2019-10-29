class Book:
    def __init__(self,title,author,publisher,year,pages,isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.isbn = isbn
        self.is_bulky = self.pages >= 500

    def is_valuable(self,year):
            if 2019 - self.year >= 20 or 2019-self.year <= 1:
                return True
            else:
               return False