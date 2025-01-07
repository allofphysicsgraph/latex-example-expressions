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


class Calc(ExprVisitor):
    def __init__(self):
        self.id_memory = {}
        self.output = []

    def visitExpr_relop_expr(self, ctx: ExprParser.Expr_relop_exprContext):
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

    def visitParens_parens(self, ctx: ExprParser.Parens_parensContext):
        print("visitParens_parens")
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitParens(self, ctx: ExprParser.ParensContext):
        print("visitParens")
        resp = self.visit(ctx.expr())
        self.output.append(resp)
        print(resp)
        return resp

    def visitInteger_var(self, ctx: ExprParser.Integer_varContext):
        print("Integer_var")
        lhs = int(ctx.INT().getText())
        rhs = sympy.Symbol(ctx.var().getText())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        print(resp)
        self.output.append(resp)
        return resp

    def visitFnctn(self, ctx: ExprParser.FnctnContext):
        print("visitFnctn")
        resp = ctx.getText()
        resp = sympy.Function(resp, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitVar_prime(self, ctx: ExprParser.Var_primeContext):
        set_trace()
        lhs = ctx.var().getText()
        rhs = ctx.PRIME().getText()
        resp = sympy.Symbol(lhs + rhs)
        self.output.append(resp)
        print(resp)
        return resp

    def visitVar_parens(self, ctx: ExprParser.Var_parensContext):
        print("visitVar_parens")
        lhs = sympy.Symbol(ctx.var().getText())
        rhs = self.visit(ctx.exp())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitInteger(self, ctx: ExprParser.IntegerContext):
        print("visitInteger")
        resp = int(ctx.INT().getText())
        self.output.append(resp)
        return resp

    def visitAdd_sub(self, ctx: ExprParser.Add_subContext):
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

    def visitBraces(self, ctx: ExprParser.BracesContext):
        print("visitBraces")
        resp = self.visit(ctx.expr())
        self.output.append(resp)
        print(resp)
        return resp

    def visitBrackets(self, ctx: ExprParser.BracketsContext):
        print("visitBrackets")
        resp = self.visit(ctx.expr())
        self.output.append(resp)
        print(resp)
        return resp

    def visitFlt(self, ctx: ExprParser.FltContext):
        print("visitFlt")
        resp = ctx.FLOAT().getText()
        l = re.findall("(\..*)", resp)
        if l:
            rnd = len(list(l[0]))
            resp = sympy.Float(resp, rnd)
            self.output.append(resp)
            print(self.output)
            return resp

    def visitParens_var(self, ctx: ExprParser.Parens_varContext):
        print("visitParens_var")
        lhs = self.visit(ctx.exp())
        rhs = sympy.Symbol(ctx.var().getText())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitBrackets_var(self, ctx: ExprParser.Brackets_varContext):
        print("visitBrackets_var")
        lhs = self.visit(ctx.exp())
        rhs = sympy.Symbol(ctx.var().getText())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitBinom(self, ctx: ExprParser.BinomContext):
        print("visitBinom")
        lhs = self.visit(ctx.binomial().numerator())
        rhs = self.visit(ctx.binomial().denominator())
        resp = sympy.binomial(lhs, rhs, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitVar_var(self, ctx: ExprParser.Var_varContext):
        print("visitVar_var")
        # set_trace()
        lhs = sympy.Symbol(ctx.var(0).getText())
        rhs = sympy.Symbol(ctx.var(1).getText())
        resp = sympy.Mul(lhs, rhs, evaluate=False)

        self.output.append(resp)
        print(resp)
        return resp

    def visitVariable(self, ctx: ExprParser.VariableContext):
        print("visitVariable")
        resp = sympy.Symbol(ctx.getText())
        self.output.append(resp)
        print(resp)
        return resp

    def visitFlt_var(self, ctx: ExprParser.Flt_varContext):
        print("visitFlt_var")
        pass

    def visitMul_div(self, ctx: ExprParser.Mul_divContext):
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

    def visitSymbl(self, ctx: ExprParser.SymblContext):
        print("visitSymbl")
        pass

    def visitExpo(self, ctx: ExprParser.ExpoContext):
        print("visitExpo")
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        resp = sympy.Pow(lhs, rhs, evaluate=False)
        print(resp)
        self.output.append(resp)
        return resp

    def visitAbs_expr(self, ctx: ExprParser.Abs_exprContext):
        print("visitAbs_expr")
        resp = self.visit(ctx.expr())
        resp = sympy.Abs(resp, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitFrac(self, ctx: ExprParser.FracContext):
        print("visitFrac")
        lhs = self.visit(ctx.fraction().numerator())
        rhs = self.visit(ctx.fraction().denominator())
        resp = sympy.Mul(lhs, sympy.Pow(rhs, -1, evaluate=False), evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitHbar(self, ctx: ExprParser.HbarContext):
        print("visitHbar")
        pass

    def visitLangle(self, ctx: ExprParser.LangleContext):
        print("visitLangle")
        pass

    def visitPsi(self, ctx: ExprParser.PsiContext):
        print("visitPsi")
        pass

    def visitVec(self, ctx: ExprParser.VecContext):
        print("visitVec")
        pass

    def visitHat(self, ctx: ExprParser.HatContext):
        print("visitHat")
        pass

    def visitFunction(self, ctx: ExprParser.FunctionContext):
        print("visitFunction")
        pass

    def visitIntegral(self, ctx: ExprParser.IntegralContext):
        print("visitIntegral")
        expr = self.visit(ctx.expr())
        var = sympy.Symbol(ctx.v.text)
        resp = sympy.Integral(expr, var)
        print(resp)

    def visitFactorial(self, ctx: ExprParser.FactorialContext):
        print("visitFactorial")
        resp = self.visit(ctx.expr())
        print(resp)
        resp = sympy.factorial(resp, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitLog(self, ctx: ExprParser.LogContext):
        print("visitLog")
        if ctx.atom():
            if ctx.atom().INT():
                e1 = int(ctx.atom().INT().getText())
            if ctx.atom().var():
                e1 = sympy.Symbol(ctx.atom().var().getText())
        else:
            e1 = self.visit(ctx.e1)
        e2 = self.visit(ctx.e2)
        resp = sympy.log(e2, e1)
        self.output.append(resp)
        print(resp)
        return resp

    def visitLg(self, ctx: ExprParser.LgContext):
        print("visitLg")
        expr = self.visit(ctx.e)
        resp = sympy.log(expr, 10)
        self.output.append(resp)
        print(resp)
        return resp

    def visitExp(self, ctx: ExprParser.ExpContext):
        print("visitExp")
        expr = self.visit(ctx.e)
        resp = sympy.exp(expr)
        self.output.append(resp)
        print(resp)
        return resp

    def visitLn(self, ctx: ExprParser.LnContext):
        print("visitLn")
        from sympy.core.numbers import E

        expr = self.visit(ctx.e)
        resp = sympy.log(expr, E)
        self.output.append(resp)
        print(resp)
        return resp

    def visitFloor(self, ctx: ExprParser.FloorContext):
        print("visitFloor")
        resp = self.visit(ctx.expr())
        resp = sympy.floor(resp, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitCeiling(self, ctx: ExprParser.CeilingContext):
        print("visitCeiling")
        resp = self.visit(ctx.expr())
        resp = sympy.ceiling(resp, evaluate=False)
        self.output.append(resp)
        print(resp)
        return resp

    def visitSin(self, ctx: ExprParser.SinContext):
        print("visitSin")
        if ctx.atom():
            print(ctx.atom().getType())
            var = ctx.atom().var().getText()
            symbol = sympy.Symbol(var)
            resp = sympy.sin(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.sin(expr)
        self.output.append(resp)
        print(resp)
        return resp

    def visitArccos(self, ctx: ExprParser.ArccosContext):
        print("visitArccos")
        pass

    def visitArccot(self, ctx: ExprParser.ArccotContext):
        print("visitArccot")
        pass

    def visitArccsc(self, ctx: ExprParser.ArccscContext):
        print("visitArccsc")
        pass

    def visitArcosh(self, ctx: ExprParser.ArcoshContext):
        print("visitArcosh")
        pass

    def visitArcsec(self, ctx: ExprParser.ArcsecContext):
        print("visitArcsec")
        pass

    def visitArcsin(self, ctx: ExprParser.ArcsinContext):
        print("visitArcsin")
        pass

    def visitArctan(self, ctx: ExprParser.ArctanContext):
        print("visitArctan")
        pass

    def visitArsinh(self, ctx: ExprParser.ArsinhContext):
        print("visitArsinh")
        pass

    def visitArtanh(self, ctx: ExprParser.ArtanhContext):
        print("visitArtanh")
        pass

    def visitCos(self, ctx: ExprParser.CosContext):
        print("visitCos")
        pass

    def visitCosh(self, ctx: ExprParser.CoshContext):
        print("visitCosh")
        pass

    def visitCot(self, ctx: ExprParser.CotContext):
        print("visitCot")
        pass

    def visitCsc(self, ctx: ExprParser.CscContext):
        print("visitCsc")
        pass

    def visitSec(self, ctx: ExprParser.SecContext):
        print("visitSec")
        pass

    def visitSinh(self, ctx: ExprParser.SinhContext):
        print("visitSinh")
        pass

    def visitTanh(self, ctx: ExprParser.TanhContext):
        print("visitTanh")
        pass

    def visitTan(self, ctx: ExprParser.TanContext):
        print("visitTan")
        pass

    def visitAtom(self, ctx: ExprParser.AtomContext):
        print("visitAtom")
        pass

    def visitSum(self, ctx: ExprParser.SumContext):
        print("visitSum")
        if ctx.e0:
            expr = self.visit(ctx.e0)

        if ctx.eq0:
            expr = self.visit(ctx.eq0)
            var = expr.args[0]
            start_index = expr.args[1]
        expr1 = self.visit(ctx.e1)
        expr2 = self.visit(ctx.e2)
        resp = sympy.Sum(expr2, (var, start_index, expr1))
        self.output.append(resp)
        print(resp)
        return resp

    def visitBinomial(self, ctx: ExprParser.BinomialContext):
        print("visitBinomial")
        pass

    def visitFraction(self, ctx: ExprParser.FractionContext):
        print("visitFraction")
        pass

    def visitNumerator_integer(self, ctx: ExprParser.Numerator_integerContext):
        print("Numerator Int")
        resp = int(ctx.getText())
        self.output.append(resp)
        return resp
        pass

    def visitNumerator_expr(self, ctx: ExprParser.Numerator_exprContext):
        print("visitNumerator_expr")
        pass

    def visitDenominator_integer(self, ctx: ExprParser.Denominator_integerContext):
        print("visitDenominator_integer")
        pass

    def visitDenominator_expr(self, ctx: ExprParser.Denominator_exprContext):
        print("visitDenominator_expr")
        pass

    def visitEquation(self, ctx: ExprParser.EquationContext):
        print("visitEquation")
        pass

    def visitRelational(self, ctx: ExprParser.RelationalContext):
        print("visitRelational")
        pass

    def visitRelop(self, ctx: ExprParser.RelopContext):
        print("visitRelop")
        pass

    def visitVar_K(self, ctx: ExprParser.Var_KContext):
        print("visitVar_K")
        pass

    def visitVar_G(self, ctx: ExprParser.Var_GContext):
        print("visitVar_G")
        pass

    def visitVar_x(self, ctx: ExprParser.Var_xContext):
        print("visitVar_x")
        pass

    def visitVar_y(self, ctx: ExprParser.Var_yContext):
        print("visitVar_y")
        pass

    def visitVar_z(self, ctx: ExprParser.Var_zContext):
        print("visitVar_z")
        pass

    def visitVar_a(self, ctx: ExprParser.Var_aContext):
        print("visitVar_a")
        pass

    def visitVar_b(self, ctx: ExprParser.Var_bContext):
        print("visitVar_b")
        pass

    def visitVar_c(self, ctx: ExprParser.Var_cContext):
        print("visitVar_c")
        pass

    def visitVar_n(self, ctx: ExprParser.Var_nContext):
        print("visitVar_n")
        pass

    def visitVar_h(self, ctx: ExprParser.Var_hContext):
        print("visitVar_h")
        pass

    def visitVar_k(self, ctx: ExprParser.Var_kContext):
        print("visitVar_k")
        pass

    def visitVar_u(self, ctx: ExprParser.Var_uContext):
        print("visitVar_u")
        pass

    def visitVar_v(self, ctx: ExprParser.Var_vContext):
        print("visitVar_v")
        pass

    def visitVar_w(self, ctx: ExprParser.Var_wContext):
        print("visitVar_w")
        pass

    def visitVar_theta(self, ctx: ExprParser.Var_thetaContext):
        print("visitVar_theta")
        pass

    def visitVar_alpha(self, ctx: ExprParser.Var_alphaContext):
        print("visitVar_alpha")
        pass

    def visitVar_beta(self, ctx: ExprParser.Var_betaContext):
        print("visitVar_beta")
        pass

    def visitVar_underscore_braces_var(
        self, ctx: ExprParser.Var_underscore_braces_varContext
    ):
        pass

    def visitVar_underscore_int(self, ctx: ExprParser.Var_underscore_intContext):
        print("visitVar_underscore_int")
        pass

    def visitVar_underscore_braces_int(
        self, ctx: ExprParser.Var_underscore_braces_intContext
    ):
        pass

    def visitVar_underscore_var(self, ctx: ExprParser.Var_underscore_varContext):
        print("visitVar_underscore_var")
        pass

    def visitVar_K(self, ctx: ExprParser.Var_KContext):
        print("visitVar_K")
        pass

    def visitVar_G(self, ctx: ExprParser.Var_GContext):
        print("visitVar_G")
        pass

    def visitVar_x(self, ctx: ExprParser.Var_xContext):
        print("visitVar_x")
        pass

    def visitVar_y(self, ctx: ExprParser.Var_yContext):
        print("visitVar_y")
        pass

    def visitVar_z(self, ctx: ExprParser.Var_zContext):
        print("visitVar_z")
        pass

    def visitVar_a(self, ctx: ExprParser.Var_aContext):
        print("visitVar_a")
        pass

    def visitVar_b(self, ctx: ExprParser.Var_bContext):
        print("visitVar_b")
        pass

    def visitVar_c(self, ctx: ExprParser.Var_cContext):
        print("visitVar_c")
        pass

    def visitVar_n(self, ctx: ExprParser.Var_nContext):
        print("visitVar_n")
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
        print("visitVar_underscore_braces_var")
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

    def visitSymbol(self, ctx):
        print("symbol")
        resp = sympy.Symbol(ctx.getText())
        self.output.append(resp)
        return resp

    def visitVar(self, ctx):
        print("Var")
        resp = sympy.Symbol(ctx.var().getText())
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
        print("Denominator Int")
        resp = int(ctx.getText())
        self.output.append(resp)
        return resp


def run_test(k):
    input_stream = InputStream(k)
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
exceptions = []
no_output = []
for ix, tpl in enumerate(GOOD_PAIRS):
    k, v = tpl

    if re.findall(r"\\limit|mathit|product", k):
        continue
    output = False

    try:
        output = run_test(k)
        if not output:
            no_ouput.append(k)
            # set_trace()
    except Exception as e:
        # set_trace()
        exceptions.append((e, k, v))
        continue
    if output:
        print(output[-1], v)
        # review types
        result = str(output[-1]) == str(v)
        if result:
            ok.append(ix)
        else:
            # set_trace()
            failed.append((output, k, v))
    # inp = input()

print(
    "ok",
    len(ok),
    "failed",
    len(failed),
    "percentage",
    100 * len(ok) / ix,
)
print(failed)
# <     def visitBraces_var(self, ctx:ExprParser.Braces_varContext): resp = ctx.getText()
# <     def visitVar_braces(self, ctx:ExprParser.Var_bracesContext): resp = ctx.getText()
