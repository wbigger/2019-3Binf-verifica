class Book:
    def __init__(self,title,author,publisher,year,pages,isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.isbn = isbn
        if self.pages > 500:
            self.is_bulky = True
        else:
            self.is_bulky = False
        

        
        

