from book import Book


il_rosso_e_il_nero = Book("Il rosso e il nero","Stendhal","Rizzoli",2010,385,"IT\\ICCU\\ANA\\0343850")
dalla_parte_di_swann = Book("Dalla parte di Swann","Marcel Proust","Rizzoli",2010,410,"IT\\ICCU\\MIL\\0802696")
books = [il_rosso_e_il_nero,dalla_parte_di_swann]
 
assert len(books) == 2, f"il libro inserito è {len(books)}, ma deve essere 1"
assert books[0].title == "Il rosso e il nero", f"Il libro è{books[0].title},deve essere 'Il rosso e il nero'"
assert books[1].title == "Dalla parte di Swann",f"Il libro è{books[1].title},deve essere 'Dalla parte di Swann'"
 
def get_book_list():
    return books