class Book:
    def __init__(self,title,author,publisher,year,pages,isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year 
        self.pages = pages
        self.isbn = isbn
        self.is_bulky = self.pages > 500
    
    def is_valuable(self,this_book):
        if this_book > 1997 and this_book < 2017:
            return True
        else:
            return False

            
    




