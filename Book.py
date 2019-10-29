class Book:
    def __init__(self, title, author, publisher, year, pages, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.isbn = isbn

        self.is_bulky = (self.pages > 500)

    def is_valuable(self, current_year):
        age = (current_year - self.year)
        return age < 1 or age > 20