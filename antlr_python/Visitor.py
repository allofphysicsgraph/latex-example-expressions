from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
import sympy
from sys import argv
from pudb import set_trace


class Calc(ExprVisitor):
    def __init__(self):
        self.id_memory = {}
        self.output = []

    def visitInteger(self, ctx):
        print("visitInteger")
        resp = int(ctx.INT().getText())
        self.output.append(resp)
        return resp

    def visitAdd_sub(self, ctx):
        print("add_sub")
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        if ctx.op.text == "+":
            resp = sympy.Add(lhs, rhs, evaluate=False)

        if ctx.op.text == "-":
            resp = sympy.Add(lhs, -1 * rhs, evaluate=False)
        self.output.append(resp)

    def visitVar(self, ctx):
        print("symbol")
        resp = sympy.Symbol(ctx.VAR().getText())
        self.output.append(resp)
        return resp


input_stream = FileStream(argv[1])
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()
parser = ExprParser(token_stream)
tree = parser.prog()
print(tree.toStringTree(recog=parser))
calc = Calc()
calc.visit(tree)
print(calc.output)
