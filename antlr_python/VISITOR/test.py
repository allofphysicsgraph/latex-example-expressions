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
import re
from test_cases import *


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

    def visitMathit_text(self, ctx: ExprParser.Mathit_textContext):
        match = re.findall(r"\\mathit{(.*?)}", ctx.getText())
        if match:
            resp = match[0]
            resp = sympy.Symbol(resp)
            self.output.append(resp)
            print(resp)
            return resp
        print("mathit_text no match")
        return resp

    def visitVariable(self, ctx: ExprParser.VariableContext):
        match = re.findall("\\mathit{(.*?)}", ctx.getText())
        if match:
            resp = match[0]
            print(match)
        else:
            resp = sympy.Symbol(ctx.getText())
        self.output.append(resp)
        print(resp)
        return resp

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
for ix, tpl in enumerate(GOOD_PAIRS):
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

print(
    "ok",
    len(ok),
    "failed",
    len(failed),
    "percentage",
    100 * len(ok) / (len(ok) + len(failed)),
)
print(failed)
#     def visitArccos(self, ctx:ExprParser.ArccosContext): resp = ctx.getText()
#     def visitArccot(self, ctx:ExprParser.ArccotContext): resp = ctx.getText()
#     def visitArccsc(self, ctx:ExprParser.ArccscContext): resp = ctx.getText()
#     def visitArcosh(self, ctx:ExprParser.ArcoshContext): resp = ctx.getText()
#     def visitArcsec(self, ctx:ExprParser.ArcsecContext): resp = ctx.getText()
#     def visitArcsin(self, ctx:ExprParser.ArcsinContext): resp = ctx.getText()
#     def visitArctan(self, ctx:ExprParser.ArctanContext): resp = ctx.getText()
#     def visitArsinh(self, ctx:ExprParser.ArsinhContext): resp = ctx.getText()
#     def visitArtanh(self, ctx:ExprParser.ArtanhContext): resp = ctx.getText()
#     def visitCos(self, ctx:ExprParser.CosContext): resp = ctx.getText()
#     def visitCosh(self, ctx:ExprParser.CoshContext): resp = ctx.getText()
#     def visitCot(self, ctx:ExprParser.CotContext): resp = ctx.getText()
#     def visitCsc(self, ctx:ExprParser.CscContext): resp = ctx.getText()
#     def visitSec(self, ctx:ExprParser.SecContext): resp = ctx.getText()
#     def visitSinh(self, ctx:ExprParser.SinhContext): resp = ctx.getText()
#     def visitTanh(self, ctx:ExprParser.TanhContext): resp = ctx.getText()
#     def visitTan(self, ctx:ExprParser.TanContext): resp = ctx.getText()
