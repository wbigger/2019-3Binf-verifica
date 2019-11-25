# Method 1: import whole file but use the full path in code
import database.anselmi

def test1():
    print(database.anselmi.Martin_Eden)
    assert len(database.anselmi.get_books_list()) == 2


# Method 2: import only the desired folder
from database.anselmi import get_books_list as get_anselmi_list

def test2():
    print(Martin_Eden) # only imported get_anselmi_list
    assert len(get_anselmi_list()) == 2

# Method 3: import whole file and use directly the identifier, wothout full path
from database.anselmi import *

def test3():
    print(Martin_Eden)
    assert len(get_books_list()) == 2