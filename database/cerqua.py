from Book import Book


book_1 = Book("i fratelli karamazov", "fedor dostoevskij", "Rizzoli", 2010, 475, "IT\\ICCU\\MIL\\0802714")
#book_2 = Book("Il fu Mattia Pascal", "Luigi Pirandello", "Mondadori", 1904, 208," IT\ICCU\RAV\1683042")

books = [book_1,book_1]
print(books[0].title,",", books[0].author)

def get_books_list():
    return books