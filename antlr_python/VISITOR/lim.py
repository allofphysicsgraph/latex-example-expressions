# grep -oP '\\[a-z]+' lim_test_cases |sort|uniq|xargs -i echo "('\\\\{}',' VARIABLE '),"
import pynini
import re
from file_utils import read_file
from sys import argv
import string
from time import sleep

sigstar = pynini.union(*string.ascii_letters + "{}_\\").closure().optimize()

resp = (
    pynini.string_map(
        [
            (" ", " "),
            ("{", "{"),
            ("}", "}"),
            ("0", "INTEGER"),
            ("1", "INTEGER"),
            ("\\alpha", " VARIABLE "),
            ("a", " VARIABLE "),
            ("\\beta", " VARIABLE "),
            ("B", " VARIABLE "),
            ("\\delta", " VARIABLE "),
            ("\\downarrow", " DOWNARROW "),
            ("d", " VARIABLE "),
            ("\\ell", " VARIABLE "),
            ("\\epsilon", " VARIABLE "),
            ("\\eps", " VARIABLE "),
            ("\\eta", " VARIABLE "),
            ("\\e", " VARIABLE "),
            ("h", " VARIABLE "),
            ("\\infty", " INFTY "),
            ("-\\infty", " NEG_INFTY "),
            ("+\\infty", " POS_INFTY "),
            ("i", " VARIABLE "),
            ("j", " VARIABLE "),
            ("J", " VARIABLE "),
            ("k", " VARIABLE "),
            ("K", " VARIABLE "),
            ("\\lambda", " VARIABLE "),
            ("\\lim_", ""),
            ("l", " VARIABLE "),
            ("L", " VARIABLE "),
            ("m", " VARIABLE "),
            ("M", " VARIABLE "),
            ("^-", " NEG "),
            ("n", " VARIABLE "),
            ("N", " VARIABLE "),
            ("\\omega", " VARIABLE "),
            ("^+", " POS "),
            ("p", " VARIABLE "),
            ("P", " VARIABLE "),
            ("q", " VARIABLE "),
            ("\\ra", " TO "),
            ("\\rho", " VARIABLE "),
            ("\\rightarrow", " TO "),
            ("r", " VARIABLE "),
            ("R", " VARIABLE "),
            ("s", " VARIABLE "),
            ("\\tau", " VARIABLE "),
            ("\\to", " TO "),
            ("t", " VARIABLE "),
            ("T", " VARIABLE "),
            ("\\uparrow", " VARIABLE "),
            ("u", " VARIABLE "),
            ("\\varepsilon", " VARIABLE "),
            ("\\varepsilon", "VARIABLE "),
            ("V", " VARIABLE "),
            ("|x|", " ABS_VARIABLE "),
            ("x", " VARIABLE "),
            ("z", " VARIABLE "),
        ]
    )
    .closure()
    .optimize()
)
with open(argv[1], "r") as f:
    data = [x.strip() for x in f.readlines()]
output = []
for line in data:
    lst = list((f"{line}" @ resp).paths().ostrings())
    if lst:
        print(line)
        print(lst)
        # sleep(1)
exit()

# from pynini.lib import rewrite
# sigstar.closure()
# sigstar.optimize()
# lexicon = pynini.union("cool","hello","\\lim","_","{","}"," ","x",'to','0').closure().optimize()
# fst1 = pynini.union(pynini.cross('\\lim_{','').closure().optimize(),lexicon).closure().optimize()
# print(list(('\\lim_{x to 0}' @ fst1).paths().ostrings()))
# variables = pynini.union('x').closure().optimize()
# rulr_1 = pynini.cross(*variables,"VAR")

# rulr = pynini.cdrewrite(pynini.union(pynini.cross("\\lim_{","LIM"),rulr1),"","",sigstar)
# print(list(('\\lim_{x \\to 0}' @rulr).paths().ostrings()))
