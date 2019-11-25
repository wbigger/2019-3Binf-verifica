from Book import Book


book_1 = Book("i fratelli karamazov", "fedor dostoevskij", "Rizzoli", 2010, 475, "IT\\ICCU\\MIL\\0802714")

books = [book_1]
print(books[0].title,",", books[0].author)
#TODO creare una funzione che si deve chiamare esattamente "get_books_list" che ritorna una lista con i file che ho creato