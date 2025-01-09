from time import sleep
from antlr4 import *
from FracLexer import FracLexer
from FracParser import FracParser
from FracVisitor import FracVisitor
import sympy
from sys import argv
from pudb import set_trace
import re
from collections import OrderedDict


class Calc(FracVisitor):
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
    lexer =FracLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = FracParser(token_stream)

    tree = parser.expr()
    print(tree.toStringTree(recog=parser))
    #calc = Calc()
    #calc.visit(tree)
    #return calc.parse_tree

run_test('\\frac23')
