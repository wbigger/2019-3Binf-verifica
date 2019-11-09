from Library import Library
from Book import Book

marconi = Library("Biblioteca IIS Marconi","CIVMA")

harry_potter = Book("Harry Potter","J.K Rowling","Salani editore",1997,350,12345)

def test_all():
    assert marconi.name == "Biblioteca IIS Marconi"
    assert marconi.sbn_code == "CIVMA"
    assert marconi.last_update != ""
    assert len(marconi.catalogue) == 0

    marconi.add_book(harry_potter)

    assert len(marconi.catalogue) == 1

