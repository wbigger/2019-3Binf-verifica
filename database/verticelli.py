from Book import Book

book_1 = Book("E ORA...TUTTI IN BRASILE", "LUIGI GARLANDO", "PIEMME", 2017, 125, "IT\\ICCU\\UBO\\4257798")
book_2 = Book("INIZIA IL CAMPIONATO", "LUIGI GARLANDO", "PIEMME", 2017, 153, "IT\\ICCU\\CAG\\2069244")
catalog = [book_1, book_2]

def get_books_list ():
    return catalog