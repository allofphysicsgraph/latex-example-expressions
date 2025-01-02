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


class Calc(ExprVisitor):
    def __init__(self):
        self.id_memory = {}
        self.output = []

    def visitInteger(self, ctx):
        print("visitInteger")
        resp = int(ctx.INT().getText())
        self.output.append(resp)
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

    def visitVar(self, ctx):
        print("symbol")
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
