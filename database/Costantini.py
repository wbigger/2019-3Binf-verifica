from Book import Book

book_01 = Book("La canzone da sei soldi ","A. J. Cronin","Bompiani",1965 , 373, "IT\\ICCU\\LIA\\0032849")
book_02 = Book("La camera cinese", "Vivian Connell", "Garzanti", 1965, 303, "IT\\ICCU\\SBL\\0553196")

books = [book_01, book_02]

def get_books_list():
    return books
