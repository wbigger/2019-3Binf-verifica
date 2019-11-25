from Book import Book

get_thinking = Book("Get_thinking", "Herbert_ruchta",
                    "Cambridge", 2012, 221, "978\\1\\108\\40299\\6")

pollyanna = Book("Pollyanna", "Eleonor_H.porter",
                 "Deagostini", 2001, 137, "88\\415\\6187\\4")

books = [get_thinking, pollyanna]


def get_books_list():
    return books
