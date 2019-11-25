from Book import Book

ritratto_di_signora = Book("Ritratto di signora","Henry James","Rizzoli",2010,404,"IT\\ICCU\\ANA\\0343679")
bel_ami = Book("Bel Ami","Guy de maupassant","Rizzoli",2010,374,"IT\\ICCU\\ANA\\0343631")

books = [ritratto_di_signora,bel_ami]

def get_books_list():
    return books
