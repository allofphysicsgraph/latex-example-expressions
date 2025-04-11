import pynini
import re
from file_utils import read_file
from sys import argv
import string
from time import sleep

sigstar = pynini.union(*string.ascii_letters + "{}_\\").closure().optimize()
fst1 = pynini.union("abc", "abd").optimize()
ascii_table = pynini.SymbolTable()
for i in range(12, 128):
    ascii_table.add_symbol(chr(i), i)
fst1.set_input_symbols(ascii_table)
fst1.draw("fst1.dot")
