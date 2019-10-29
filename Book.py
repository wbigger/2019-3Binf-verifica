class Book:
    def __init__(self,title,author,publisher,year,pages,isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.isbn = isbn
        self.is_bulky = pages > 500
        
                
    def is_valuable(self,current_year):
        if current_year > self.year + 20 or current_year < self.year + 1:
            return True
        else:
            return False

    

    

                
                
        