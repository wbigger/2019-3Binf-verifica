from Book import Book

il_processo = Book("Il processo", "Franz Kafka", "Rizzoli", 2009, 266, "IT\\ICCU\\ANA\\0328832")
cuore_di_tenebra = Book("Cuore di tenebra La linea d'ombra", "Joseph Conrad", "Rizzoli", 2009, 282, "IT\\ICCU\\MIL\\0797139")

books = [il_processo, cuore_di_tenebra]


assert len(books) == 2, f"i libri inseriti sono {len(books)}, ma devono essere 2"
assert books[0].title == "Il processo", f"il primo libro è{books[0].title}, dovrebbe essere 'Il processo'" 
assert books[1].title == "Cuore di tenebra La linea d'ombra", f"il primo libro è{books[0].title}, dovrebbe essere 'Cuore di tenebra La linea d'ombra'"

def get_books_list():
    return books