from Book import Book

il_processo = Book("Il processo", "Franz Kafka", "Rizzoli", 2009, 266, "IT\\ICCU\\ANA\\0328832")
cuore_di_tenebra = Book("Cuore di tenebra La linea d'ombra", "Joseph Conrad", "Rizzoli", 2009, 282, "IT\\ICCU\\MIL\\0797139")

books = [il_processo, cuore_di_tenebra]

assert len(books) == 2, "i libri inseriti sono {}, ma devono essere 2".format(len(books))
assert books[0].title == "Il processo", "il primo libro e' {}, dovrebbe essere 'Il processo'" .format(books[0].title)
assert books[1].title == "Cuore di tenebra La linea d'ombra", "il primo libro e' {}, dovrebbe essere 'Cuore di tenebra La linea d'ombra'".format({books[0].title})

def get_books_list():
    return books