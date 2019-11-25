from Book import Book

i_fratelli_karamazov = Book("I fratelli karamazov", "Fëdor Dostoevskij", "Rizzoli", 2010, 442, "IT\\ICCU\\MIL\\0802705")
ivanhoe = Book("Ivanhoe", "Walter Scott", "Rizzoli", 2009, 480, "IT\\ICCU\\ANA\\0328827")

books = [i_fratelli_karamazov, ivanhoe]

assert books[0] == i_fratelli_karamazov
assert books[1] == ivanhoe

def get_books_list():
    return books