from Book import Book

i_fratelli_karamazov = Book("I Fratelli Karamazov", "Fedor Dostoevskij", "Rizzoli", 2010, 374, "IT\\ICCU\\IEI\\0472625")
il_rosso_e_il_nero = Book("Il rosso e il nero", "Stendhal", "Rizzoli", 2010, 388, "IT\\ICCU\\MOD\\0738722")

books = [i_fratelli_karamazov, il_rosso_e_il_nero]

assert books[0] == i_fratelli_karamazov
assert books[1] == il_rosso_e_il_nero

def get_books_list(the_list):
    return books
    