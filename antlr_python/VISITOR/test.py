# antlr4 -no-listener -visitor Expr.g4 -Dlanguage=Python3tom

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
from collections import OrderedDict


class Calc(ExprVisitor):
    def __init__(self):
        self.parse_tree = OrderedDict()

    def logger(self, ctx, resp):
        start = ctx.start.tokenIndex
        stop = ctx.stop.tokenIndex
        name = type(ctx).__name__
        text = ctx.getText()
        self.parse_tree[(name, start, stop)] = (text, resp)

    def visitExpr_relop_expr(self, ctx: ExprParser.Expr_relop_exprContext):
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
        self.logger(ctx, resp)
        return resp

    def visitParens_parens(self, ctx: ExprParser.Parens_parensContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitParens(self, ctx: ExprParser.ParensContext):
        resp = self.visit(ctx.expr())
        self.logger(ctx, resp)
        return resp

    def visitInteger_var(self, ctx: ExprParser.Integer_varContext):
        lhs = int(ctx.INT().getText())
        rhs = self.visit(ctx.var())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitFnctn(self, ctx: ExprParser.FnctnContext):
        resp = ctx.getText()
        resp = sympy.Function(resp, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitVar_prime(self, ctx: ExprParser.Var_primeContext):
        lhs = self.visit(ctx.var())
        rhs = ctx.PRIME().getText()
        resp = sympy.Symbol(lhs + rhs)
        self.logger(ctx, resp)
        return resp

    def visitVar_parens(self, ctx: ExprParser.Var_parensContext):
        lhs = self.visit(ctx.var())
        rhs = self.visit(ctx.expr())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitVar_G(self, ctx: ExprParser.Var_GContext):
        resp = ctx.G().getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_a(self, ctx: ExprParser.Var_aContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_b(self, ctx: ExprParser.Var_bContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_c(self, ctx: ExprParser.Var_cContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_x(self, ctx: ExprParser.Var_xContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_y(self, ctx: ExprParser.Var_yContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_z(self, ctx: ExprParser.Var_zContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_u(self, ctx: ExprParser.Var_uContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_v(self, ctx: ExprParser.Var_vContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_w(self, ctx: ExprParser.Var_wContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_n(self, ctx: ExprParser.Var_nContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_h(self, ctx: ExprParser.Var_hContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_K(self, ctx: ExprParser.Var_KContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_k(self, ctx: ExprParser.Var_kContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_alpha(self, ctx: ExprParser.Var_alphaContext):
        resp = ctx.getText()
        resp = re.sub(r"\\+", "", resp)
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_theta(self, ctx: ExprParser.Var_thetaContext):
        # set_trace()
        resp = ctx.getText()
        resp = re.sub(r"\\+", "", resp)
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitInteger(self, ctx: ExprParser.IntegerContext):
        resp = int(ctx.INT().getText())
        self.logger(ctx, resp)
        return resp

    def visitAdd_sub(self, ctx: ExprParser.Add_subContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        if ctx.op.text == "+":
            resp = sympy.Add(lhs, rhs, evaluate=False)
        if ctx.op.text == "-":
            resp = sympy.Add(lhs, -1 * rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitBraces(self, ctx: ExprParser.BracesContext):
        resp = self.visit(ctx.expr())
        self.logger(ctx, resp)
        return resp

    def visitBrackets(self, ctx: ExprParser.BracketsContext):
        resp = self.visit(ctx.expr())
        self.logger(ctx, resp)
        return resp

    def visitFlt(self, ctx: ExprParser.FltContext):
        resp = ctx.FLOAT().getText()
        l = re.findall("(\..*)", resp)
        if l:
            rnd = len(list(l[0]))
            resp = sympy.Float(resp, rnd)
            self.logger(ctx, resp)
            return resp

    def visitParens_var(self, ctx: ExprParser.Parens_varContext):
        lhs = self.visit(ctx.expr())
        rhs = sympy.Symbol(ctx.var().getText())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitBraces_var(self, ctx: ExprParser.Braces_varContext):
        lhs = self.visit(ctx.expr())
        rhs = sympy.Symbol(ctx.var().getText())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitBrackets_var(self, ctx: ExprParser.Brackets_varContext):
        lhs = self.visit(ctx.expr())
        rhs = sympy.Symbol(ctx.var().getText())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitBinom(self, ctx: ExprParser.BinomContext):
        lhs = self.visit(ctx.binomial().numerator())
        rhs = self.visit(ctx.binomial().denominator())
        resp = sympy.binomial(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitVar_var(self, ctx: ExprParser.Var_varContext):
        lhs = self.visit(ctx.var(0))
        rhs = self.visit(ctx.var(1))
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitVariable(self, ctx: ExprParser.VariableContext):
        resp = sympy.Symbol(ctx.getText())
        self.logger(ctx, resp)
        return resp

    def visitFlt_var(self, ctx: ExprParser.Flt_varContext):
        # set_trace()
        lhs = ctx.FLOAT().getText()
        rhs = sympy.Symbol(ctx.var().getText())
        l = re.findall("(\..*)", lhs)
        if l:
            rnd = len(list(l[0]))
            lhs = sympy.Float(lhs, rnd)
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitMul_div(self, ctx: ExprParser.Mul_divContext):
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
        self.logger(ctx, resp)
        return resp

    def visitSymbl(self, ctx: ExprParser.SymblContext):
        pass

    def visitExpo(self, ctx: ExprParser.ExpoContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        resp = sympy.Pow(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitAbs_expr(self, ctx: ExprParser.Abs_exprContext):
        resp = self.visit(ctx.expr())
        resp = sympy.Abs(resp, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitFrac(self, ctx: ExprParser.FracContext):
        lhs = self.visit(ctx.fraction().numerator())
        rhs = self.visit(ctx.fraction().denominator())
        resp = sympy.Mul(lhs, sympy.Pow(rhs, -1, evaluate=False), evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitHbar(self, ctx: ExprParser.HbarContext):
        pass

    def visitLangle(self, ctx: ExprParser.LangleContext):
        pass

    def visitPsi(self, ctx: ExprParser.PsiContext):
        pass

    def visitVec(self, ctx: ExprParser.VecContext):
        pass

    def visitHat(self, ctx: ExprParser.HatContext):
        pass

    def visitFunction(self, ctx: ExprParser.FunctionContext):
        pass

    def visitIntegral(self, ctx: ExprParser.IntegralContext):
        expr = self.visit(ctx.expr())
        var = sympy.Symbol(ctx.v.text)
        resp = sympy.Integral(expr, var)
        set_trace()

    def visitFactorial(self, ctx: ExprParser.FactorialContext):
        resp = self.visit(ctx.expr())
        resp = sympy.factorial(resp, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitLog(self, ctx: ExprParser.LogContext):
        if ctx.atom():
            if ctx.atom().INT():
                e1 = int(ctx.atom().INT().getText())
            if ctx.atom().var():
                e1 = sympy.Symbol(ctx.atom().var().getText())
        else:
            e1 = self.visit(ctx.e1)
        e2 = self.visit(ctx.e2)
        resp = sympy.log(e2, e1, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitLimit(self, ctx: ExprParser.LimitContext):
        var = sympy.Symbol(ctx.var().getText())
        expr1 = self.visit(ctx.e1)
        expr2 = self.visit(ctx.e2)
        direction = "+-"
        if ctx.PLUS():
            direction = "+"
        if ctx.MINUS():
            direction = "-"
        resp = sympy.Limit(expr2, var, expr1, dir=direction)
        self.logger(ctx, resp)
        return resp

    def visitLg(self, ctx: ExprParser.LgContext):
        expr = self.visit(ctx.e)
        resp = sympy.log(expr, 10, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitExp(self, ctx: ExprParser.ExpContext):
        expr = self.visit(ctx.e)
        resp = sympy.exp(expr)
        self.logger(ctx, resp)
        return resp

    def visitLn(self, ctx: ExprParser.LnContext):
        from sympy.core.numbers import E

        expr = self.visit(ctx.e)
        resp = sympy.log(expr, E, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitFloor(self, ctx: ExprParser.FloorContext):
        resp = self.visit(ctx.expr())
        resp = sympy.floor(resp, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitCeiling(self, ctx: ExprParser.CeilingContext):
        resp = self.visit(ctx.expr())
        resp = sympy.ceiling(resp, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitSin(self, ctx: ExprParser.SinContext):
        # set_trace()
        if ctx.atom():
            symbol = self.visit(ctx.atom())
            resp = sympy.sin(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.sin(expr)
        self.logger(ctx, resp)
        return resp

    def visitArccos(self, ctx: ExprParser.ArccosContext):
        if ctx.atom():
            var = self.visit(ctx.atom())
            resp = sympy.acos(var)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.acos(expr)
        self.logger(ctx, resp)
        return resp
        pass

    def visitArccot(self, ctx: ExprParser.ArccotContext):
        if ctx.atom():
            var = self.visit(ctx.atom())
            resp = sympy.acot(var)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.acot(expr)
        self.logger(ctx, resp)
        return resp

    def visitArccsc(self, ctx: ExprParser.ArccscContext):
        if ctx.atom():
            var = self.visit(ctx.atom())
            resp = sympy.acsc(var)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.acsc(expr)
        self.logger(ctx, resp)
        return resp

    def visitArcosh(self, ctx: ExprParser.ArcoshContext):
        if ctx.atom():
            var = self.visit(ctx.atom())
            resp = sympy.acosh(var)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.acosh(expr)
        self.logger(ctx, resp)
        return resp

    def visitArcsec(self, ctx: ExprParser.ArcsecContext):
        pass

    def visitArcsin(self, ctx: ExprParser.ArcsinContext):
        pass

    def visitArctan(self, ctx: ExprParser.ArctanContext):
        pass

    def visitArsinh(self, ctx: ExprParser.ArsinhContext):
        pass

    def visitArtanh(self, ctx: ExprParser.ArtanhContext):
        if ctx.atom():
            var = ctx.atom().var().getText()
            symbol = sympy.Symbol(var)
            resp = sympy.atanh(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.atanh(expr)
        self.logger(ctx, resp)
        return resp

    def visitCos(self, ctx: ExprParser.CosContext):
        if ctx.atom():
            var = ctx.atom().var().getText()
            symbol = sympy.Symbol(var)
            resp = sympy.cos(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.cos(expr)
        self.logger(ctx, resp)
        return resp

    def visitCosh(self, ctx: ExprParser.CoshContext):
        if ctx.atom():
            var = ctx.atom().var().getText()
            symbol = sympy.Symbol(var)
            resp = sympy.cosh(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.cosh(expr)
        self.logger(ctx, resp)
        return resp

    def visitCot(self, ctx: ExprParser.CotContext):
        if ctx.atom():
            var = ctx.atom().var().getText()
            symbol = sympy.Symbol(var)
            resp = sympy.cot(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.cot(expr)
        self.logger(ctx, resp)
        return resp

    def visitCsc(self, ctx: ExprParser.CscContext):
        if ctx.atom():
            var = ctx.atom().var().getText()
            symbol = sympy.Symbol(var)
            resp = sympy.csc(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.csc(expr)
        self.logger(ctx, resp)
        return resp

    def visitSec(self, ctx: ExprParser.SecContext):
        if ctx.atom():
            var = ctx.atom().var().getText()
            symbol = sympy.Symbol(var)
            resp = sympy.sec(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.sec(expr)
        self.logger(ctx, resp)
        return resp

    def visitSinh(self, ctx: ExprParser.SinhContext):
        if ctx.atom():
            var = ctx.atom().var().getText()
            symbol = sympy.Symbol(var)
            resp = sympy.sinh(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.sinh(expr)
        self.logger(ctx, resp)
        return resp

    def visitTanh(self, ctx: ExprParser.TanhContext):
        if ctx.atom():
            var = ctx.atom().var().getText()
            symbol = sympy.Symbol(var)
            resp = sympy.tanh(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.tanh(expr)
        self.logger(ctx, resp)
        return resp

    def visitTan(self, ctx: ExprParser.TanContext):
        if ctx.atom():
            var = self.visit(ctx.atom())
            symbol = sympy.Symbol(var)
            resp = sympy.tan(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.tan(expr)
        self.logger(ctx, resp)
        return resp

    def visitAtom(self, ctx: ExprParser.AtomContext):
        # set_trace()
        if ctx.var():
            resp = self.visit(ctx.var())
        if ctx.INT():
            resp = self.visit(ctx.INT())
        if ctx.FLOAT():
            resp = self.visit(ctx.FLOAT())
        self.logger(ctx, resp)
        return resp

    def visitSum(self, ctx: ExprParser.SumContext):
        if ctx.e0:
            expr = self.visit(ctx.e0)
        if ctx.eq0:
            expr = self.visit(ctx.eq0)
            var = expr.args[0]
            start_index = expr.args[1]
        expr1 = self.visit(ctx.e1)
        expr2 = self.visit(ctx.e2)
        resp = sympy.Sum(expr2, (var, start_index, expr1))
        self.logger(ctx, resp)
        return resp

    def visitBinomial(self, ctx: ExprParser.BinomialContext):
        pass

    def visitFraction(self, ctx: ExprParser.FractionContext):
        pass

    def visitNumerator_integer(self, ctx: ExprParser.Numerator_integerContext):
        resp = int(ctx.getText())
        self.logger(ctx, resp)
        return resp

    def visitNumerator_expr(self, ctx: ExprParser.Numerator_exprContext):
        pass

    def visitDenominator_integer(self, ctx: ExprParser.Denominator_integerContext):
        pass

    def visitDenominator_expr(self, ctx: ExprParser.Denominator_exprContext):
        pass

    def visitEquation(self, ctx: ExprParser.EquationContext):
        pass

    def visitRelational(self, ctx: ExprParser.RelationalContext):
        pass

    def visitRelop(self, ctx: ExprParser.RelopContext):
        pass

    def visitVar_underscore_braces_var(
        self, ctx: ExprParser.Var_underscore_braces_varContext
    ):
        pass

    def visitVar_underscore_int(self, ctx: ExprParser.Var_underscore_intContext):
        pass

    def visitVar_underscore_braces_int(
        self, ctx: ExprParser.Var_underscore_braces_intContext
    ):
        pass

    def visitVar_underscore_var(self, ctx: ExprParser.Var_underscore_varContext):
        pass

    def visitVar_underscore_braces_var(
        self, ctx: ExprParser.Var_underscore_braces_varContext
    ):
        resp = sympy.Symbol(ctx.getText())
        self.logger(ctx, resp)
        return resp

    def visitVar_underscore_int(self, ctx: ExprParser.Var_underscore_intContext):
        lhs = ctx.getChild(0).getText() + ctx.getChild(1).getText()
        rhs = "{" + ctx.getChild(2).getText() + "}"
        resp = sympy.Symbol(lhs + rhs)
        self.logger(ctx, resp)
        return resp

    def visitVar_underscore_braces_int(
        self, ctx: ExprParser.Var_underscore_braces_intContext
    ):
        resp = sympy.Symbol(ctx.getText())
        self.logger(ctx, resp)
        return resp

    def visitVar_underscore_var(self, ctx: ExprParser.Var_underscore_varContext):
        lhs = ctx.getChild(0).getText() + ctx.getChild(1).getText()
        rhs = "{" + ctx.getChild(2).getText() + "}"
        resp = sympy.Symbol(lhs + rhs)
        self.logger(ctx, resp)
        return resp

    def visitSymbol(self, ctx):
        resp = sympy.Symbol(ctx.getText())
        self.logger(ctx, resp)
        return resp

    def visitVar(self, ctx):
        text = self.visit(ctx.var())
        resp = sympy.Symbol(text)
        self.logger(ctx, resp)
        return resp

    def visitEquation(self, ctx):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        resp = sympy.Eq(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitNumerator_expr(self, ctx):
        resp = self.visit(ctx.expr())
        self.logger(ctx, resp)
        return resp

    def visitDenominator_expr(self, ctx):
        resp = self.visit(ctx.expr())
        self.logger(ctx, resp)
        return resp

    def visitDenominator_integer(self, ctx):
        resp = int(ctx.getText())
        self.logger(ctx, resp)
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
    return calc.parse_tree


from time import sleep

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
            print(d)
            if repr(resp) == repr(v):
                ok.append((k, v))
            else:
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
set_trace()
print(failed)
# <     def visitProduct(self, ctx:ExprParser.ProductContext): resp = ctx.getText()
# <     def visitPi(self, ctx:ExprParser.PiContext): resp = ctx.getText()
# <     def visitInfty(self, ctx:ExprParser.InftyContext): resp = ctx.getText()
# <     def visitOverline(self, ctx:ExprParser.OverlineContext): resp = ctx.getText()
# <     def visitLimit(self, ctx:ExprParser.LimitContext): resp = ctx.getText()
# <     def visitSqrt(self, ctx:ExprParser.SqrtContext): resp = ctx.getText()
