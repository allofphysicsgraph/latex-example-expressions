# antlr4 -no-listener -visitor LaTeX.g4 -Dlanguage=Python3
from antlr4 import *
from collections import OrderedDict
from LaTeXLexer import LaTeXLexer
from LaTeXParser import LaTeXParser
from LaTeXParserVisitor import LaTeXParserVisitor
from pudb import set_trace
from sys import argv
from test_cases import *
from time import sleep
import re
import sympy


class Calc(LaTeXParserVisitor):
    def __init__(self):
        self.parse_tree = OrderedDict()

    def logger(self, ctx, resp):
        start = ctx.start.tokenIndex
        stop = ctx.stop.tokenIndex
        name = type(ctx).__name__
        text = ctx.getText()
        self.parse_tree[(name, start, stop)] = (text, resp)


def run_test(k):
    input_stream = InputStream(k)
    lexer = LaTeXLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = LaTeXParser(token_stream)
    tree = parser.prog()
    # print(tree.toStringTree(recog=parser))
    calc = Calc()
    calc.visit(tree)
    return calc.parse_tree


ok = []
failed = []
exceptions = []
no_output = []
# debug = True
debug = False
for ix, tpl in enumerate(GOOD_PAIRS):
    k, v = tpl
    if re.findall(r"\\int|\\prod|angle|sqrt|\\lim|\\infty|mathit|product", k):
        continue
    output = False
    try:
        d = run_test(k)
        if d:
            resp = d[list(d)[-1]][-1]
            if repr(resp) == repr(v):
                ok.append((k, v))
            else:
                print(d)
                print(k, resp, v)
                if debug:
                    inp = input("trace?")
                    print(d)
                    if inp != "":
                        set_trace()
                failed.append(k)
        else:
            failed.append(k)

    except Exception as e:
        print(k)
        print(e)

print(
    "ok",
    len(ok),
    "failed",
    len(failed),
    "percentage",
    100 * len(ok) / ix,
)
# set_trace()
print(failed)
