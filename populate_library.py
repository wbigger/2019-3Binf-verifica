from Library import Library

from database.anselmi import get_books_list as get_anselmi # error in book order (risolto)
from database.cacchiarelli import get_books_list as get_cacchiarelli 
from database.cerqua import get_books_list as get_cerqua # manca funzione
from database.cicio import get_books_list as get_cicio
from database.cioineag import get_books_list as get_cioineag # typos (risolti)
from database.costantini import get_books_list as get_costantini
from database.dionisi import get_books_list as get_dionisi
from database.gasparri import get_books_list as get_gasparri
from database.lupu import get_books_list as get_lupu
from database.miglietta import get_books_list as get_miglietta # typos (risolti)
#from database.miheev import get_books_list as get_miheev
from database.perna import get_books_list as get_perna
from database.salernitano import get_books_list as get_salernitano
from database.teti import get_books_list as get_teti # typos (risolti)
#from database.tullio import get_books_list as get_tullio
from database.verticelli import get_books_list as get_verticelli # typos (risolti)


marconi = Library("Biblioteca IIS Marconi", "CIVMA")
expected_catalogue_len = 0
assert len(marconi.catalogue) == expected_catalogue_len

marconi.add_books(get_anselmi())
expected_catalogue_len += 2
assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

marconi.add_books(get_cacchiarelli())
expected_catalogue_len += 2
assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

# marconi.add_books(get_cerqua())
# expected_catalogue_len += 2
# assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

marconi.add_books(get_cicio())
expected_catalogue_len += 2
assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

marconi.add_books(get_cioineag())
expected_catalogue_len += 2
assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

marconi.add_books(get_costantini())
expected_catalogue_len += 2
assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

marconi.add_books(get_dionisi())
expected_catalogue_len += 2
assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

# marconi.add_books(get_gasparri())
# expected_catalogue_len += 2
# assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

marconi.add_books(get_lupu())
expected_catalogue_len += 2
assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

marconi.add_books(get_miglietta())
expected_catalogue_len += 2
assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

# marconi.add_books(get_miheev())
# expected_catalogue_len += 2
# assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

# marconi.add_books(get_perna())
# expected_catalogue_len += 2
# assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

marconi.add_books(get_salernitano())
expected_catalogue_len += 2
assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

marconi.add_books(get_teti())
expected_catalogue_len += 2
assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

# marconi.add_books(get_tullio())
# expected_catalogue_len += 2
# assert len(marconi.catalogue) == expected_catalogue_len, f"Expected {expected_catalogue_len}, got {len(marconi.catalogue)}"

marconi.add_books(get_verticelli())
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
