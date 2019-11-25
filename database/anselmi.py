from Book import Book

martin_eden = Book("Martin_Eden","Jack_London","Rizzoli",2010,460,"IT\\ICCU\\TO0\\0417044")
ritratto_di_signora_II = Book("Henry_James","Ritratto_di_Signora_II","",2010,355,"IT\\ICCU\\ANA\\0343680")

books = [martin_eden,ritratto_di_signora_II]

def get_books_list():
    return books
