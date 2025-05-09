import pynini
import re
from file_utils import read_file
from sys import argv
import string
from time import sleep

sigstar = pynini.union(*string.ascii_letters + "/(){}_^=-+\\").closure().optimize()

resp = (
    pynini.string_map(
        [
            (r"\\begin{equation}", " "),
            (r"\\end{equation}", " "),
            (" ", " "),
            ("&", " AMPRESAND "),
            (".", " DOT "),
            ("|", "|"),
            ("*", " TIMES "),
            ("~", " tilde "),
            ("'", " PRIME "),
            ("\\", "\\"),
            ("w", " VARIABLE "),
            ("\\mathcal", " "),
            ("\\rm ", " "),
            ("D", " VARIABLE "),
            ("E", " VARIABLE "),
            ("H", " VARIABLE "),
            ("C", " VARIABLE "),
            ("T", " VARIABLE "),
            ("b", " VARIABLE "),
            ("g", " VARIABLE "),
            ("U", " VARIABLE "),
            ("C", " VARIABLE "),
            ("I", " VARIABLE "),
            ("W", " VARIABLE "),
            ("v", " VARIABLE "),
            ("\\Delta", " DELTA_UC "),
            (" ", " "),
            ("S", " VARIABLE "),
            ("0", " INTEGER "),
            ("1", " INTEGER "),
            ("2", " INTEGER "),
            ("3", " INTEGER "),
            ("4", " INTEGER "),
            ("5", " INTEGER "),
            ("6", " INTEGER "),
            ("7", " INTEGER "),
            ("8", " INTEGER "),
            ("9", " INTEGER "),
            ("\\alpha", " ALPHA "),
            ("a", " VARIABLE "),
            ("A", " VARIABLE "),
            ("\\beta", " BETA "),
            ("\\bf", " BF "),
            ("\\bm", " BM "),
            ("B", " VARIABLE "),
            ("\\cal", " CAL "),
            ("c", " CONSTANT "),
            ("\\cdot", " CDOT "),
            ("\\cfrac", " CFRAC "),
            ("\\chi", " CHI "),
            (",", " COMMA "),
            ("\\delta", " DELTA "),
            ("/", " DIV "),
            ("\\downarrow", " DOWNARROW "),
            ("d", " VARIABLE "),
            ("\\epsilon", " EPSILON "),
            ("=", " EQUALS "),
            ("\\eta", " ETA "),
            ("e", " VARIABLE "),
            ("E", " VARIABLE "),
            ("\\exp", ""),
            ("f", " FUNC "),
            ("\\frac", " FRAC "),
            ("F", " VARIABLE "),
            ("\\gamma", " GAMMA "),
            ("\\Gamma", " GAMMA_UC "),
            ("\\hat", " HAT "),
            ("\\hbar", " HBAR "),
            ("h", " VARIABLE "),
            ("H", " VARIABLE "),
            ("\\imath", " IMATH "),
            ("\\infty", " INFTY "),
            ("-\\infty", " NEG_INFTY "),
            ("+\\infty", " POS_INFTY "),
            ("i", " VARIABLE "),
            ("j", " VARIABLE "),
            ("J", " VARIABLE "),
            ("\\kappa", " KAPPA "),
            ("k", " VARIABLE "),
            ("K", " VARIABLE "),
            ("\\lambda", " LAMBDA "),
            ("\\nabla", " NABLA "),
            ("\\Lambda", " LAMBDA_UC "),
            ("\\langle", " LANGLE "),
            ("{", " LB "),
            ("\\log", " LOG "),
            ("(", "LP"),
            ("<", " LT "),
            ("l", " VARIABLE "),
            ("L", " VARIABLE "),
            ("+", " MINUS "),
            ("-", " MINUS "),
            ("\\mp", " MP "),
            ("\\mu", " MU "),
            ("m", " VARIABLE "),
            ("M", " VARIABLE "),
            ("^-", " NEG "),
            ("\\neq", " NEQ "),
            ("\\nu", " NU "),
            ("n", " VARIABLE "),
            ("N", " VARIABLE "),
            ("\\omega", " OMEGA "),
            ("o", " VARIABLE "),
            ("\\phi", " PHI "),
            ("\\pi", " PI "),
            ("\\pm", " PM "),
            ("^+", " POS "),
            ("\\prime", " PRIME "),
            ("\\psi", " PSI "),
            ("p", " VARIABLE "),
            ("P", " VARIABLE "),
            ("q", " VARIABLE "),
            ("Q", " VARIABLE "),
            ("\\rangle", " RANGLE "),
            ("\\ra", " TO "),
            ("}", " RB "),
            ("\\rho", " RHO "),
            ("\\rightarrow", " TO "),
            ("\\rm", " RM "),
            (")", "RP"),
            ("\\r", " R "),
            ("r", " VARIABLE "),
            ("R", " VARIABLE "),
            ("\\sigma", " SIGMA "),
            ("\\sqrt", " SQRT "),
            ("_", " SUB "),
            ("^", " SUP "),
            ("s", " VARIABLE "),
            ("\\tau", " TAU "),
            ("\\text", " TEXT "),
            ("\\theta", " THETA "),
            ("\\tilde", " TILDE "),
            ("\\to", " TO "),
            ("t", " VARIABLE "),
            ("T", " VARIABLE "),
            ("\\uparrow", " UPARROW "),
            ("u", " VARIABLE "),
            ("\\varepsilon", " VAREPSILON "),
            ("\\varphi", " VARPHI "),
            ("\\vec", " VEC "),
            ("V", " VARIABLE "),
            ("\\w", " W "),
            ("|x|", " ABS_VARIABLE "),
            ("\\xi", " XI "),
            ("x", " VARIABLE "),
            ("\\x", " X "),
            ("y", " VARIABLE "),
            ("\\zeta", " ZETA "),
            ("z", " VARIABLE "),
            ("Z", " VARIABLE "),
        ]
    )
    .closure()
    .optimize()
)
with open(argv[1], "r") as f:
    data = [x.strip() for x in f.readlines()]
output = []
print(data)
for line in data:
    lst = list((f"{line}" @ resp).paths().ostrings())
    if lst:
        #print(line)
        print(lst[-1])

    if not lst:
        print(line)
        exit()
        try:
            for ix in range(len(line) - 3):
                test_case = line[: 3 + ix]
                lst2 = list((f"{test_case}" @ resp).paths().ostrings())
                if not lst2:
                    print("fails on:\t" + test_case)
        except Exception as e:
            print(e)
print('*'*50)
exit()
