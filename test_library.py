from Library import Library
from Book import Book

def test_all():
    marconi = Library("Biblioteca IIS Marconi","CIVMA")

    harry_potter = Book("Harry Potter qualcosa","JKR","Salani",1997,350,12345)



    assert marconi.name =="Biblioteca IIS Marconi"
    assert marconi.sbn_code == "CIVMA"
    assert marconi.last_update != ""
    assert len(marconi.catalogue) == 0

    marconi.add_book(harry_potter)


    assert len(marconi.catalogue) == 1