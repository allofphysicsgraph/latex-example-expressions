# antlr4 -no-listener -visitor Expr.g4 -Dlanguage=Python3

"""
(prog (stat (expr (expr (expr (expr (expr 1) + (expr 3)) + (expr 1)) + (expr x)) + (expr (expr 2) * (expr 3))) \n))
add_sub
add_sub
add_sub
add_sub
visitInteger
visitInteger
visitInteger
symbol
mul_div
visitInteger
visitInteger
[1, 3, 1 + 3, 1, 1 + (1 + 3), x, x + (1 + (1 + 3)), 2, 3, 2*3, (x + (1 + (1 + 3))) + 2*3]
"""

from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
import sympy
from sys import argv
from pudb import set_trace

from sympy.testing.pytest import XFAIL
from sympy.parsing.latex.lark import parse_latex_lark
from sympy.external import import_module

from sympy.concrete.products import Product
from sympy.concrete.summations import Sum
from sympy.core.function import Derivative, Function
from sympy.core.numbers import E, oo, Rational
from sympy.core.power import Pow
from sympy.core.parameters import evaluate
from sympy.core.relational import (
    GreaterThan,
    LessThan,
    StrictGreaterThan,
    StrictLessThan,
    Unequality,
)
from sympy.core.symbol import Symbol
from sympy.functions.combinatorial.factorials import binomial, factorial
from sympy.functions.elementary.complexes import Abs, conjugate
from sympy.functions.elementary.exponential import exp, log
from sympy.functions.elementary.integers import ceiling, floor
from sympy.functions.elementary.miscellaneous import root, sqrt, Min, Max
from sympy.functions.elementary.trigonometric import asin, cos, csc, sec, sin, tan
from sympy.integrals.integrals import Integral
from sympy.series.limits import Limit
from sympy import Matrix, MatAdd, MatMul, Transpose, Trace
from sympy import I

from sympy.core.relational import Eq, Ne, Lt, Le, Gt, Ge
from sympy.physics.quantum import Bra, Ket, InnerProduct
from sympy.abc import x, y, z, a, b, c, d, t, k, n


def run_test(k):
    print(k)
    input_stream = InputStream(k)
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = ExprParser(token_stream)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))
    calc = Calc()
    calc.visit(tree)
    print(calc.output)


def _Min(*args):
    return Min(*args, evaluate=False)


def _Max(*args):
    return Max(*args, evaluate=False)


def _log(a, b=E):
    if b == E:
        return log(a, evaluate=False)
    else:
        return log(a, b, evaluate=False)


def _MatAdd(a, b):
    return MatAdd(a, b, evaluate=False)


def _MatMul(a, b):
    return MatMul(a, b, evaluate=False)


class Calc(ExprVisitor):
    def __init__(self):
        self.id_memory = {}
        self.output = []

    def visitVariable(self, ctx: ExprParser.VariableContext):
        pass

    def visitVar_K(self, ctx: ExprParser.Var_KContext):
        pass

    def visitVar_G(self, ctx: ExprParser.Var_GContext):
        pass

    def visitVar_x(self, ctx: ExprParser.Var_xContext):
        pass

    def visitVar_y(self, ctx: ExprParser.Var_yContext):
        pass

    def visitVar_z(self, ctx: ExprParser.Var_zContext):
        pass

    def visitVar_a(self, ctx: ExprParser.Var_aContext):
        pass

    def visitVar_b(self, ctx: ExprParser.Var_bContext):
        pass

    def visitVar_c(self, ctx: ExprParser.Var_cContext):
        pass

    def visitVar_n(self, ctx: ExprParser.Var_nContext):
        pass

    def visitVar_h(self, ctx: ExprParser.Var_hContext):
        pass

    def visitVar_k(self, ctx: ExprParser.Var_kContext):
        pass

    def visitVar_u(self, ctx: ExprParser.Var_uContext):
        pass

    def visitVar_v(self, ctx: ExprParser.Var_vContext):
        pass

    def visitVar_w(self, ctx: ExprParser.Var_wContext):
        pass

    def visitVar_theta(self, ctx: ExprParser.Var_thetaContext):
        pass

    def visitVar_alpha(self, ctx: ExprParser.Var_alphaContext):
        pass

    def visitVar_beta(self, ctx: ExprParser.Var_betaContext):
        pass

    def visitVar_underscore_braces_var(
        self, ctx: ExprParser.Var_underscore_braces_varContext
    ):
        resp = sympy.Symbol(ctx.getText())
        self.output.append(resp)
        print(resp)
        return resp

    def visitVar_underscore_int(self, ctx: ExprParser.Var_underscore_intContext):
        lhs = ctx.getChild(0).getText() + ctx.getChild(1).getText()
        rhs = "{" + ctx.getChild(2).getText() + "}"
        resp = sympy.Symbol(lhs + rhs)
        self.output.append(resp)
        print(resp)
        return resp

    def visitVar_underscore_braces_int(
        self, ctx: ExprParser.Var_underscore_braces_intContext
    ):
        resp = sympy.Symbol(ctx.getText())
        self.output.append(resp)
        print(resp)
        return resp

    def visitVar_underscore_var(self, ctx: ExprParser.Var_underscore_varContext):
        lhs = ctx.getChild(0).getText() + ctx.getChild(1).getText()
        rhs = "{" + ctx.getChild(2).getText() + "}"
        resp = sympy.Symbol(lhs + rhs)
        self.output.append(resp)
        print(resp)
        return resp

    def visitInteger(self, ctx):
        print("visitInteger")
        resp = int(ctx.INT().getText())
        self.output.append(resp)
        return resp

    def visitExpr_relop_expr(self, ctx):
        print("expr_relop_expr")
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        if ctx.op.text == "\\neq":
            resp = sympy.Ne(lhs, rhs, evaluate=False)
        if ctx.op.text == "<":
            resp = sympy.Lt(lhs, rhs, evaluate=False)
        if ctx.op.text == ">":
            resp = sympy.Gt(lhs, rhs, evaluate=False)
        if ctx.op.text == "\\le":
            resp = sympy.Le(lhs, rhs, evaluate=False)
        if ctx.op.text == "\\ge":
            resp = sympy.Ge(lhs, rhs, evaluate=False)
        if ctx.op.text == "\\leq":
            resp = sympy.Le(lhs, rhs, evaluate=False)
        if ctx.op.text == "\\geq":
            resp = sympy.Ge(lhs, rhs, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitMul_div(self, ctx):
        print("mul_div")
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        if ctx.op.text == "*":
            resp = sympy.Mul(lhs, rhs, evaluate=False)
        if ctx.op.text == "\\cdot":
            resp = sympy.Mul(lhs, rhs, evaluate=False)
        if ctx.op.text == "\\times":
            resp = sympy.Mul(lhs, rhs, evaluate=False)
        if ctx.op.text == "/":
            resp = sympy.Mul(lhs, sympy.Pow(rhs, -1, evaluate=False), evaluate=False)
        if ctx.op.text == "\\div":
            resp = sympy.Mul(lhs, sympy.Pow(rhs, -1, evaluate=False), evaluate=False)
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
        print(resp)
        return resp

    def visitSymbol(self, ctx):
        print("symbol")
        resp = sympy.Symbol(ctx.getText())
        self.output.append(resp)
        return resp

    def visitVar(self, ctx):
        print("Var")
        resp = sympy.Symbol(ctx.VAR().getText())
        self.output.append(resp)
        return resp

    def visitEquation(self, ctx):
        print("equals")
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        resp = sympy.Eq(lhs, rhs, evaluate=False)
        print(resp)
        self.output.append(resp)
        return resp

    def visitExpo(self, ctx):
        print("expo")
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        resp = sympy.Pow(lhs, rhs, evaluate=False)
        print(resp)
        self.output.append(resp)
        return resp

    def visitInteger_var(self, ctx):
        print("Integer_var")
        lhs = int(ctx.INT().getText())
        rhs = sympy.Symbol(ctx.VAR().getText())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        print(resp)
        self.output.append(resp)
        return resp

    def visitNumerator_integer(self, ctx):
        print("Numerator Int")
        resp = int(ctx.getText())
        self.output.append(resp)
        return resp

    def visitNumerator_expr(self, ctx):
        print("Numerator Expr")
        resp = self.visit(ctx.expr())
        self.output.append(resp)
        return resp

    def visitDenominator_expr(self, ctx):
        print("Denominator Expr")
        resp = self.visit(ctx.expr())
        self.output.append(resp)
        return resp

    def visitDenominator_integer(self, ctx):
        # set_trace()
        print("Denominator Int")
        resp = int(ctx.getText())
        self.output.append(resp)
        return resp

    def visitBinom(self, ctx):
        lhs = self.visit(ctx.binomial().numerator())
        rhs = self.visit(ctx.binomial().denominator())
        resp = sympy.binomial(lhs, rhs, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitFrac(self, ctx):
        lhs = self.visit(ctx.fraction().numerator())
        rhs = self.visit(ctx.fraction().denominator())
        resp = sympy.Mul(lhs, sympy.Pow(rhs, -1, evaluate=False), evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitParens_parens(self, ctx):
        # set_trace()
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitAbs_expr(self, ctx):
        resp = self.visit(ctx.expr())
        resp = sympy.Abs(resp, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitParens(self, ctx):
        resp = self.visit(ctx.expr())
        self.output.append(resp)
        print(resp)
        return resp

    def visitBraces(self, ctx):
        resp = self.visit(ctx.expr())
        self.output.append(resp)
        print(resp)
        return resp

    def visitFactorial(self, ctx):
        # set_trace()
        resp = self.visit(ctx.expr())
        print(resp)
        resp = sympy.factorial(resp, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitVar_var(self, ctx):
        # set_trace()
        lhs = sympy.Symbol(ctx.VAR(0).getText())
        rhs = sympy.Symbol(ctx.VAR(1).getText())
        resp = sympy.Mul(lhs, rhs, evaluate=False)

        self.output.append(resp)
        print(resp)
        return resp

    def visitIntegral(self, ctx):
        expr = self.visit(ctx.expr())
        var = sympy.Symbol(ctx.v.text)
        resp = sympy.Integral(expr, var)
        print(resp)

    def visitLg(self, ctx: ExprParser.LgContext):
        # set_trace()
        expr = self.visit(ctx.e)
        resp = sympy.log(expr, 10)
        self.output.append(resp)
        print(resp)
        return resp

    def visitLn(self, ctx: ExprParser.LnContext):
        # set_trace()
        from sympy.core.numbers import E

        expr = self.visit(ctx.e)
        resp = sympy.log(expr, E)
        self.output.append(resp)
        print(resp)
        return resp

    def visitSin(self, ctx: ExprParser.SinContext):
        if ctx.atom():
            print(ctx.atom().getType())
            var = ctx.atom().VAR().getText()
            symbol = sympy.Symbol(var)
            resp = sympy.sin(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.sin(expr)

        self.output.append(resp)
        print(resp)
        return resp

    def visitExp(self, ctx: ExprParser.ExpContext):
        # set_trace()
        expr = self.visit(ctx.e)
        resp = sympy.exp(expr)
        self.output.append(resp)
        print(resp)
        return resp

    def visitSum(self, ctx: ExprParser.SumContext):
        if ctx.e0:
            expr = self.visit(ctx.e0)

        if ctx.eq0:
            expr = self.visit(ctx.eq0)
            var = expr.args[0]
            start_index = expr.args[1]
            # set_trace()
        expr1 = self.visit(ctx.e1)
        expr2 = self.visit(ctx.e2)
        resp = sympy.Sum(expr2, (var, start_index, expr1))
        print(resp)
        # print(expr,expr1,expr2)

    def visitLog(self, ctx: ExprParser.LogContext):

        if ctx.atom():
            if ctx.atom().INT():
                e1 = int(ctx.atom().INT().getText())
            if ctx.atom().VAR():
                e1 = sympy.Symbol(ctx.atom().VAR().getText())
        else:
            e1 = self.visit(ctx.e1)
        e2 = self.visit(ctx.e2)
        resp = sympy.log(e2, e1)
        self.output.append(resp)
        print(resp)
        return resp

    def visitFloor(self, ctx: ExprParser.FloorContext):
        resp = self.visit(ctx.expr())
        self.output.append(resp)
        print(resp)
        return sympy.floor(resp, evaluate=False)

    def visitCeiling(self, ctx: ExprParser.CeilingContext):
        resp = self.visit(ctx.expr())
        self.output.append(resp)
        print(resp)
        return sympy.ceiling(resp, evaluate=False)

    def visitFnctn(self, ctx: ExprParser.FunctionContext):

        resp = ctx.getText()
        self.output.append(resp)
        print(resp)
        return sympy.Function(resp, evaluate=False)


# These LaTeX strings should parse to the corresponding SymPy expression
SYMBOL_EXPRESSION_PAIRS = [
    (r"x_0", Symbol("x_{0}")),
    (r"x_{1}", Symbol("x_{1}")),
    (r"x_a", Symbol("x_{a}")),
    (r"x_{b}", Symbol("x_{b}")),
    (r"h_\theta", Symbol("h_{theta}")),
    (r"h_{\theta}", Symbol("h_{theta}")),
    (r"y''_1", Symbol("y''_{1}")),
    (r"y_1''", Symbol("y_{1}''")),
    (r"\mathit{x}", Symbol("x")),
    (r"\mathit{test}", Symbol("test")),
    (r"\mathit{TEST}", Symbol("TEST")),
    (r"\mathit{HELLO world}", Symbol("HELLO world")),
    (r"a'", Symbol("a'")),
    (r"a''", Symbol("a''")),
    (r"\alpha'", Symbol("alpha'")),
    (r"\alpha''", Symbol("alpha''")),
    (r"a_b", Symbol("a_{b}")),
    (r"a_b'", Symbol("a_{b}'")),
    (r"a'_b", Symbol("a'_{b}")),
    (r"a'_b'", Symbol("a'_{b}'")),
    (r"a_{b'}", Symbol("a_{b'}")),
    (r"a_{b'}'", Symbol("a_{b'}'")),
    (r"a'_{b'}", Symbol("a'_{b'}")),
    (r"a'_{b'}'", Symbol("a'_{b'}'")),
    (r"\mathit{foo}'", Symbol("foo'")),
    (r"\mathit{foo'}", Symbol("foo'")),
    (r"\mathit{foo'}'", Symbol("foo''")),
    (r"a_b''", Symbol("a_{b}''")),
    (r"a''_b", Symbol("a''_{b}")),
    (r"a''_b'''", Symbol("a''_{b}'''")),
    (r"a_{b''}", Symbol("a_{b''}")),
    (r"a_{b''}''", Symbol("a_{b''}''")),
    (r"a''_{b''}", Symbol("a''_{b''}")),
    (r"a''_{b''}'''", Symbol("a''_{b''}'''")),
    (r"\mathit{foo}''", Symbol("foo''")),
    (r"\mathit{foo''}", Symbol("foo''")),
    (r"\mathit{foo''}'''", Symbol("foo'''''")),
    (r"a_\alpha", Symbol("a_{alpha}")),
    (r"a_\alpha'", Symbol("a_{alpha}'")),
    (r"a'_\alpha", Symbol("a'_{alpha}")),
    (r"a'_\alpha'", Symbol("a'_{alpha}'")),
    (r"a_{\alpha'}", Symbol("a_{alpha'}")),
    (r"a_{\alpha'}'", Symbol("a_{alpha'}'")),
    (r"a'_{\alpha'}", Symbol("a'_{alpha'}")),
    (r"a'_{\alpha'}'", Symbol("a'_{alpha'}'")),
    (r"a_\alpha''", Symbol("a_{alpha}''")),
    (r"a''_\alpha", Symbol("a''_{alpha}")),
    (r"a''_\alpha'''", Symbol("a''_{alpha}'''")),
    (r"a_{\alpha''}", Symbol("a_{alpha''}")),
    (r"a_{\alpha''}''", Symbol("a_{alpha''}''")),
    (r"a''_{\alpha''}", Symbol("a''_{alpha''}")),
    (r"a''_{\alpha''}'''", Symbol("a''_{alpha''}'''")),
    (r"\alpha_b", Symbol("alpha_{b}")),
    (r"\alpha_b'", Symbol("alpha_{b}'")),
    (r"\alpha'_b", Symbol("alpha'_{b}")),
    (r"\alpha'_b'", Symbol("alpha'_{b}'")),
    (r"\alpha_{b'}", Symbol("alpha_{b'}")),
    (r"\alpha_{b'}'", Symbol("alpha_{b'}'")),
    (r"\alpha'_{b'}", Symbol("alpha'_{b'}")),
    (r"\alpha'_{b'}'", Symbol("alpha'_{b'}'")),
    (r"\alpha_b''", Symbol("alpha_{b}''")),
    (r"\alpha''_b", Symbol("alpha''_{b}")),
    (r"\alpha''_b'''", Symbol("alpha''_{b}'''")),
    (r"\alpha_{b''}", Symbol("alpha_{b''}")),
    (r"\alpha_{b''}''", Symbol("alpha_{b''}''")),
    (r"\alpha''_{b''}", Symbol("alpha''_{b''}")),
    (r"\alpha''_{b''}'''", Symbol("alpha''_{b''}'''")),
    (r"\alpha_\beta", Symbol("alpha_{beta}")),
    (r"\alpha_{\beta}", Symbol("alpha_{beta}")),
    (r"\alpha_{\beta'}", Symbol("alpha_{beta'}")),
    (r"\alpha_{\beta''}", Symbol("alpha_{beta''}")),
    (r"\alpha'_\beta", Symbol("alpha'_{beta}")),
    (r"\alpha'_{\beta}", Symbol("alpha'_{beta}")),
    (r"\alpha'_{\beta'}", Symbol("alpha'_{beta'}")),
    (r"\alpha'_{\beta''}", Symbol("alpha'_{beta''}")),
    (r"\alpha''_\beta", Symbol("alpha''_{beta}")),
    (r"\alpha''_{\beta}", Symbol("alpha''_{beta}")),
    (r"\alpha''_{\beta'}", Symbol("alpha''_{beta'}")),
    (r"\alpha''_{\beta''}", Symbol("alpha''_{beta''}")),
    (r"\alpha_\beta'", Symbol("alpha_{beta}'")),
    (r"\alpha_{\beta}'", Symbol("alpha_{beta}'")),
    (r"\alpha_{\beta'}'", Symbol("alpha_{beta'}'")),
    (r"\alpha_{\beta''}'", Symbol("alpha_{beta''}'")),
    (r"\alpha'_\beta'", Symbol("alpha'_{beta}'")),
    (r"\alpha'_{\beta}'", Symbol("alpha'_{beta}'")),
    (r"\alpha'_{\beta'}'", Symbol("alpha'_{beta'}'")),
    (r"\alpha'_{\beta''}'", Symbol("alpha'_{beta''}'")),
    (r"\alpha''_\beta'", Symbol("alpha''_{beta}'")),
    (r"\alpha''_{\beta}'", Symbol("alpha''_{beta}'")),
    (r"\alpha''_{\beta'}'", Symbol("alpha''_{beta'}'")),
    (r"\alpha''_{\beta''}'", Symbol("alpha''_{beta''}'")),
    (r"\alpha_\beta''", Symbol("alpha_{beta}''")),
    (r"\alpha_{\beta}''", Symbol("alpha_{beta}''")),
    (r"\alpha_{\beta'}''", Symbol("alpha_{beta'}''")),
    (r"\alpha_{\beta''}''", Symbol("alpha_{beta''}''")),
    (r"\alpha'_\beta''", Symbol("alpha'_{beta}''")),
    (r"\alpha'_{\beta}''", Symbol("alpha'_{beta}''")),
    (r"\alpha'_{\beta'}''", Symbol("alpha'_{beta'}''")),
    (r"\alpha'_{\beta''}''", Symbol("alpha'_{beta''}''")),
    (r"\alpha''_\beta''", Symbol("alpha''_{beta}''")),
    (r"\alpha''_{\beta}''", Symbol("alpha''_{beta}''")),
    (r"\alpha''_{\beta'}''", Symbol("alpha''_{beta'}''")),
    (r"\alpha''_{\beta''}''", Symbol("alpha''_{beta''}''")),
]


def run_test():
    input_stream = FileStream("test_file")
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = ExprParser(token_stream)
    tree = parser.prog()
    # print(tree.toStringTree(recog=parser))
    calc = Calc()
    calc.visit(tree)
    return calc.output


ok = []
failed = []
for ix, tpl in enumerate(SYMBOL_EXPRESSION_PAIRS):
    k, v = tpl
    print(k)
    f = open("test_file", "w")
    f.write(k)
    f.write("\n")
    f.close()
    try:
        output = run_test()
    except:
        failed.append((k, v))
        continue
    print(output)
    if output:
        print(output[-1], v)
        result = output[-1] == v
        if result:
            ok.append(ix)
    else:
        failed.append((k, v))
    # inp = input()

print("ok", len(ok), "failed", len(failed), "percentage", 100 * len(ok) / len(failed))
print(failed)
