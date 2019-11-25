from Library import Library

from database.anselmi import get_books_list as get_anselmi
from database.Cicio import get_books_list as get_cicio

marconi = Library("Biblioteca IIS Marconi", "CIVMA")
expected_catalogue_len = 0
assert len(marconi.catalogue) == expected_catalogue_len

marconi.add_books(get_anselmi())
expected_catalogue_len += 2
assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

marconi.add_books(get_cicio())
expected_catalogue_len += 2
assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

# a = "ciao"
# b = bin(7)
# c = True.bit_length()
# d = 7.0.fromhex("12")
# print("{} is {}".format(type(a),hex(id(a))))
# print("{} is {}".format(b,hex(id(b))))
# print("{} is {}".format(c,hex(id(c))))
# print("{} is {}".format(d,hex(id(d))))
# print("{} is {}".format(marconi.catalogue,hex(id(marconi.catalogue))))
