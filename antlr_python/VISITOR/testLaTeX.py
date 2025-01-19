# antlr4 -no-lestener -visitor LaTeX.g4 -Dlanguage=Python3
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

    def visitAtom(self, ctx: LaTeXParser.AtomContext):
        if ctx.variable():
            resp = sympy.Symbol(ctx.variable().getText())
        self.logger(ctx, resp)
        return resp

    def visitBinop(self, ctx: LaTeXParser.BinopContext):
        # set_trace()
        resp = ctx.getText()
        self.logger(ctx, resp)
        return self.visitChildren(ctx)

    def visitConstant(self, ctx: LaTeXParser.ConstantContext):
        # set_trace()
        resp = ctx.getText()
        self.logger(ctx, resp)
        return self.visitChildren(ctx)

    def visitEnclosed_expression(self, ctx: LaTeXParser.Enclosed_expressionContext):
        # set_trace()
        resp = ctx.getText()
        self.logger(ctx, resp)
        return self.visitChildren(ctx)

    def visitEquation(self, ctx: LaTeXParser.EquationContext):
        # set_trace()
        resp = ctx.getText()
        self.logger(ctx, resp)
        return self.visitChildren(ctx)

    def visitExpression(self, ctx: LaTeXParser.ExpressionContext):
        # set_trace()
        resp = ctx.getText()
        self.logger(ctx, resp)
        return self.visitChildren(ctx)

    def visitNumber(self, ctx: LaTeXParser.NumberContext):
        # set_trace()
        if ctx.INTEGER():
            resp = int(ctx.INTEGER().getText())
        self.logger(ctx, resp)
        return self.visitChildren(ctx)

    def visitNumeric_atom(self, ctx: LaTeXParser.Numeric_atomContext):
        # set_trace()
        # visits Number

        resp = ctx.getText()
        self.logger(ctx, resp)
        return self.visitChildren(ctx)

    def visitProg(self, ctx: LaTeXParser.ProgContext):
        # set_trace()
        resp = ctx.getText()
        self.logger(ctx, ctx.getText())
        return self.visitChildren(ctx)

    def visitRelop(self, ctx: LaTeXParser.RelopContext):
        # set_trace()
        resp = ctx.getText()
        self.logger(ctx, resp)
        return self.visitChildren(ctx)

    def visitSignedAtom(self, ctx: LaTeXParser.SignedAtomContext):
        # set_trace()
        resp = ctx.getText()
        self.logger(ctx, resp)
        return self.visitChildren(ctx)

    def visitVariable(self, ctx: LaTeXParser.VariableContext):
        # set_trace()
        resp = ctx.getText()
        self.logger(ctx, resp)
        return self.visitChildren(ctx)


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
