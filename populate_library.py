from Library import Library 

from database.anselmi import get_books_list as get_anselmi
from database.Cicio import get_books_list as get_cicio

marconi = Library("Biblioteca IIS Marconi", "CIVMA")
assert len(marconi.catalogue) == 0

marconi.add_books(get_anselmi())
assert len(marconi.catalogue) == 2

marconi.add_books(get_cicio())
assert len(marconi.catalogue) == 4

# a = "ciao"
# b = bin(7)
# c = True.bit_length()
# d = 7.0.fromhex("12")
# print("{} is {}".format(type(a),hex(id(a))))
# print("{} is {}".format(b,hex(id(b))))
# print("{} is {}".format(c,hex(id(c))))
# print("{} is {}".format(d,hex(id(d))))
# print("{} is {}".format(marconi.catalogue,hex(id(marconi.catalogue))))