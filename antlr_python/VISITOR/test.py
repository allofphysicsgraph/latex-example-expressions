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

from time import sleep
from antlr4 import *
from ExprLexer import ExprLexer
from ModeTagsLexer import ModeTagsLexer
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

    def visitAbs_expr(self, ctx: ExprParser.Abs_exprContext):
        resp = self.visit(ctx.expr())
        resp = sympy.Abs(resp, evaluate=False)
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

    def visitArccos(self, ctx: ExprParser.ArccosContext):
        if ctx.atom():
            atom = self.visit(ctx.atom())
            resp = sympy.acos(atom)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.acos(expr)
        self.logger(ctx, resp)
        return resp

    def visitArccot(self, ctx: ExprParser.ArccotContext):
        if ctx.atom():
            atom = self.visit(ctx.atom())
            resp = sympy.acot(atom)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.acot(expr)
        self.logger(ctx, resp)
        return resp

    def visitArccsc(self, ctx: ExprParser.ArccscContext):
        if ctx.atom():
            atom = self.visit(ctx.atom())
            resp = sympy.acsc(atom)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.acsc(expr)
        self.logger(ctx, resp)
        return resp

    def visitArcosh(self, ctx: ExprParser.ArcoshContext):
        if ctx.atom():
            atom = self.visit(ctx.atom())
            resp = sympy.acosh(atom)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.acosh(expr)
        self.logger(ctx, resp)
        return resp

    def visitArcsec(self, ctx: ExprParser.ArcsecContext):
        if ctx.atom():
            var = self.visit(ctx.atom())
            symbol = sympy.Symbol(atom)
            resp = sympy.asec(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.asec(expr)
        self.logger(ctx, resp)
        return resp

    def visitArcsin(self, ctx: ExprParser.ArcsinContext):
        if ctx.atom():
            var = self.visit(ctx.atom())
            symbol = sympy.Symbol(atom)
            resp = sympy.asin(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.asin(expr)
        self.logger(ctx, resp)
        return resp
        return self.visitChildren(ctx)

    def visitArctan(self, ctx: ExprParser.ArctanContext):
        if ctx.atom():
            var = self.visit(ctx.atom())
            symbol = sympy.Symbol(atom)
            resp = sympy.atan(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.atan(expr)
        self.logger(ctx, resp)
        return resp

    def visitArsinh(self, ctx: ExprParser.ArsinhContext):
        if ctx.atom():
            var = self.visit(ctx.atom())
            symbol = sympy.Symbol(atom)
            resp = sympy.asinh(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.asinh(expr)
        self.logger(ctx, resp)
        return resp


    def visitArtanh(self, ctx: ExprParser.ArtanhContext):
        if ctx.atom():
            var = self.visit(ctx.atom())
            symbol = sympy.Symbol(atom)
            resp = sympy.atanh(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.atanh(expr)
        self.logger(ctx, resp)
        return resp

    def visitAtom(self, ctx: ExprParser.AtomContext):
        if ctx.var():
            resp = self.visit(ctx.var())
        if ctx.INT():
            resp = self.visit(ctx.INT())
        if ctx.FLOAT():
            resp = self.visit(ctx.FLOAT())
        self.logger(ctx, resp)
        return resp

    def visitBraces(self, ctx: ExprParser.BracesContext):
        resp = self.visit(ctx.expr())
        self.logger(ctx, resp)
        return resp

    def visitBraces_var(self, ctx: ExprParser.Braces_varContext):
        lhs = self.visit(ctx.expr())
        rhs = self.visit(ctx.var())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitBrackets(self, ctx: ExprParser.BracketsContext):
        resp = self.visit(ctx.expr())
        self.logger(ctx, resp)
        return resp

    def visitBrackets_var(self, ctx: ExprParser.Brackets_varContext):
        lhs = self.visit(ctx.expr())
        rhs = self.visit(ctx.var())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitCeiling(self, ctx: ExprParser.CeilingContext):
        resp = self.visit(ctx.expr())
        resp = sympy.ceiling(resp, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitClng(self, ctx: ExprParser.ClngContext):
        return self.visitChildren(ctx)

    def visitCos(self, ctx: ExprParser.CosContext):
        if ctx.atom():
            atom = self.visit(ctx.atom())
            resp = sympy.cos(atom)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.cos(expr)
        self.logger(ctx, resp)
        return resp

    def visitCosh(self, ctx: ExprParser.CoshContext):
        if ctx.atom():
            atom = self.visit(ctx.atom())
            symbol = sympy.Symbol(atom)
            resp = sympy.cosh(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.cosh(expr)
        self.logger(ctx, resp)
        return resp

    def visitCot(self, ctx: ExprParser.CotContext):
        if ctx.atom():
            atom = self.visit(ctx.atom())
            symbol = sympy.Symbol(atom)
            resp = sympy.cot(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.cot(expr)
        self.logger(ctx, resp)
        return resp

    def visitCsc(self, ctx: ExprParser.CscContext):
        if ctx.atom():
            atom = self.visit(ctx.atom())
            symbol = sympy.Symbol(atom)
            resp = sympy.csc(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.csc(expr)
        self.logger(ctx, resp)
        return resp

    def visitDenominator_expr(self, ctx):
        resp = self.visit(ctx.expr())
        self.logger(ctx, resp)
        return resp

    def visitEqtn(self, ctx: ExprParser.EqtnContext):
        return self.visitChildren(ctx)

    def visitEquation(self, ctx: ExprParser.EquationContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        resp = sympy.Eq(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitExp(self, ctx: ExprParser.ExpContext):
        expr = self.visit(ctx.e)
        resp = sympy.exp(expr)
        self.logger(ctx, resp)
        return resp

    def visitExpo(self, ctx: ExprParser.ExpoContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        resp = sympy.Pow(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

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

    def visitExpression(self, ctx: ExprParser.ExpressionContext):
        return self.visitChildren(ctx)

    def visitFactorial(self, ctx: ExprParser.FactorialContext):
        resp = self.visit(ctx.factorial().expr())
        resp = sympy.factorial(resp, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitFactorial_recursive(self, ctx: ExprParser.Factorial_recursiveContext):
        # set_trace()
        if ctx.factorial().factorial():
            resp = self.visitFactorial(ctx.factorial())
            resp = sympy.factorial(resp, evaluate=False)
            self.logger(ctx, resp)
            return resp

    def visitFactorial_single(self, ctx: ExprParser.Factorial_singleContext):
        return self.visitChildren(ctx)

    def visitFctrl(self, ctx: ExprParser.FctrlContext):
        return self.visitChildren(ctx)

    def visitFloor(self, ctx: ExprParser.FloorContext):
        resp = self.visit(ctx.expr())
        resp = sympy.floor(resp, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitFlr(self, ctx: ExprParser.FlrContext):
        return self.visitChildren(ctx)

    def visitFlt(self, ctx: ExprParser.FltContext):
        resp = ctx.FLOAT().getText()
        l = re.findall("(\\..*)", resp)
        if l:
            rnd = len(list(l[0]))
            resp = sympy.Float(resp, rnd)
            self.logger(ctx, resp)
            return resp

    def visitFlt_var(self, ctx: ExprParser.Flt_varContext):
        # set_trace()
        lhs = ctx.FLOAT().getText()
        rhs = sympy.Symbol(ctx.var().getText())
        l = re.findall("(\\..*)", lhs)
        if l:
            rnd = len(list(l[0]))
            lhs = sympy.Float(lhs, rnd)
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitFnc_nrml(self, ctx: ExprParser.Fnc_nrmlContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#func_normal.
    def visitFnctn(self, ctx: ExprParser.FnctnContext):
        resp = ctx.getText()
        resp = sympy.Function(resp, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitFrac(self, ctx: ExprParser.FracContext):
        set_trace()
        lhs = self.visit(ctx.fraction().numerator())
        rhs = self.visit(ctx.fraction().denominator())
        resp = sympy.Mul(lhs, sympy.Pow(rhs, -1, evaluate=False), evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitFraction(self, ctx: ExprParser.FractionContext):
        set_trace()
        return self.visitChildren(ctx)

    def visitFunc_normal(self, ctx: ExprParser.Func_normalContext):
        return self.visitChildren(ctx)

    def visitFunction(self, ctx: ExprParser.FunctionContext):
        return self.visitChildren(ctx)

    def visitHat(self, ctx: ExprParser.HatContext):
        return self.visitChildren(ctx)

    def visitHbar(self, ctx: ExprParser.HbarContext):
        return self.visitChildren(ctx)

    def visitInfty(self, ctx: ExprParser.InftyContext):
        return self.visitChildren(ctx)

    def visitInteger(self, ctx: ExprParser.IntegerContext):
        # set_trace()
        resp = int(ctx.INT().getText())
        self.logger(ctx, resp)
        return resp

    def visitInteger_var(self, ctx: ExprParser.Integer_varContext):
        lhs = self.visit(ctx)
        rhs = self.visit(ctx.var())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitIntegral(self, ctx: ExprParser.IntegralContext):
        return self.visitChildren(ctx)

    def visitLangle(self, ctx: ExprParser.LangleContext):
        return self.visitChildren(ctx)

    def visitLg(self, ctx: ExprParser.LgContext):
        expr = self.visit(ctx.e)
        resp = sympy.log(expr, 10, evaluate=False)
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

    def visitLn(self, ctx: ExprParser.LnContext):
        from sympy.core.numbers import E

        expr = self.visit(ctx.e)
        resp = sympy.log(expr, E, evaluate=False)
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

    def visitNumerator_expr(self, ctx):
        resp = self.visit(ctx.expr())
        self.logger(ctx, resp)
        return resp

    def visitOverline(self, ctx: ExprParser.OverlineContext):
        return self.visitChildren(ctx)

    def visitParens(self, ctx: ExprParser.ParensContext):
        resp = self.visit(ctx.expr())
        self.logger(ctx, resp)
        return resp

    def visitParens_parens(self, ctx: ExprParser.Parens_parensContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitParens_var(self, ctx: ExprParser.Parens_varContext):
        lhs = self.visit(ctx.expr())
        rhs = sympy.Symbol(ctx.var().getText())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitPi(self, ctx: ExprParser.PiContext):
        return self.visitChildren(ctx)

    def visitProduct(self, ctx: ExprParser.ProductContext):
        return self.visitChildren(ctx)

    def visitProg(self, ctx: ExprParser.ProgContext):
        return self.visitChildren(ctx)

    def visitPsi(self, ctx: ExprParser.PsiContext):
        return self.visitChildren(ctx)

    def visitRelational(self, ctx: ExprParser.RelationalContext):
        return self.visitChildren(ctx)

    def visitRelop(self, ctx: ExprParser.RelopContext):
        return self.visitChildren(ctx)

    def visitSec(self, ctx: ExprParser.SecContext):
        if ctx.atom():
            atom = self.visit(ctx.atom())
            symbol = sympy.Symbol(atom)
            resp = sympy.sec(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.sec(expr)
        self.logger(ctx, resp)
        return resp

    def visitSin(self, ctx: ExprParser.SinContext):
        if ctx.trig_function():
            trig_fnctn = self.visit(ctx.trig_function())
            resp = sympy.sin(trig_fnctn)
        if ctx.atom():
            atom = self.visit(ctx.atom())
            resp = sympy.sin(atom)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.sin(expr)
        self.logger(ctx, resp)
        return resp

    def visitSinh(self, ctx: ExprParser.SinhContext):
        if ctx.atom():
            atom = self.visit(ctx.atom())
            symbol = sympy.Symbol(atom)
            resp = sympy.sinh(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.sinh(expr)
        self.logger(ctx, resp)
        return resp

    def visitSqrt(self, ctx: ExprParser.SqrtContext):
        return self.visitChildren(ctx)

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

    def visitSymbl(self, ctx: ExprParser.SymblContext):
        return self.visitChildren(ctx)

    def visitSymbol(self, ctx):
        resp = sympy.Symbol(ctx.getText())
        self.logger(ctx, resp)
        return resp

    def visitTan(self, ctx: ExprParser.TanContext):
        if ctx.atom():
            atom = self.visit(ctx.atom())
            symbol = sympy.Symbol(atom)
            resp = sympy.tan(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.tan(expr)
        self.logger(ctx, resp)
        return resp

    def visitTanh(self, ctx: ExprParser.TanhContext):
        if ctx.atom():
            atom = self.visit(ctx.atom())
            symbol = sympy.Symbol(atom)
            resp = sympy.tanh(symbol)
        if ctx.expr():
            expr = self.visit(ctx.expr())
            resp = sympy.tanh(expr)
        self.logger(ctx, resp)
        return resp

    def visitTrig_function(self, ctx: ExprParser.Trig_functionContext):
        return self.visitChildren(ctx)

    def visitTrig_function_multi(self, ctx: ExprParser.Trig_function_multiContext):
        lhs = self.visit(ctx.trig_function(0))
        rhs = self.visit(ctx.trig_function(1))
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitTrig_function_single(self, ctx: ExprParser.Trig_function_singleContext):
        return self.visitChildren(ctx)

    def visitTrig_parens_parens(self, ctx: ExprParser.Trig_parens_parensContext):
        print(ctx.getText())
        #set_trace()

    def visitVar(self, ctx):
        text = self.visit(ctx.var())
        resp = sympy.Symbol(text)
        self.logger(ctx, resp)
        return resp

    def visitVar_G(self, ctx: ExprParser.Var_GContext):
        resp = ctx.G().getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_K(self, ctx: ExprParser.Var_KContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_a(self, ctx: ExprParser.Var_aContext):
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

    def visitVar_b(self, ctx: ExprParser.Var_bContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_beta(self, ctx: ExprParser.Var_betaContext):
        resp = ctx.getText()
        resp = re.sub(r"\\+", "", resp)
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return self.visitChildren(ctx)

    def visitVar_braces(self, ctx: ExprParser.Var_bracesContext):
        return self.visitChildren(ctx)

    def visitVar_c(self, ctx: ExprParser.Var_cContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_h(self, ctx: ExprParser.Var_hContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_k(self, ctx: ExprParser.Var_kContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_n(self, ctx: ExprParser.Var_nContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_parens(self, ctx: ExprParser.Var_parensContext):
        lhs = self.visit(ctx.var())
        rhs = self.visit(ctx.expr())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitVar_prime(self, ctx: ExprParser.Var_primeContext):
        lhs = self.visit(ctx.var())
        rhs = ctx.PRIME().getText()
        resp = sympy.Symbol(lhs + rhs)
        self.logger(ctx, resp)
        return resp

    def visitVar_theta(self, ctx: ExprParser.Var_thetaContext):
        resp = ctx.getText()
        resp = re.sub(r"\\+", "", resp)
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_u(self, ctx: ExprParser.Var_uContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_underscore_braces_int(
        self, ctx: ExprParser.Var_underscore_braces_intContext
    ):
        resp = sympy.Symbol(ctx.getText())
        self.logger(ctx, resp)
        return resp

    def visitVar_underscore_braces_var(
        self, ctx: ExprParser.Var_underscore_braces_varContext
    ):
        resp = sympy.Symbol(ctx.getText())
        self.logger(ctx, resp)
        return resp

    def visitVar_underscore_int(self, ctx: ExprParser.Var_underscore_intContext):
        # rewrite x_1 -> x_{1}
        lhs = ctx.getChild(0).getText() + ctx.getChild(1).getText()
        rhs = "{" + ctx.getChild(2).getText() + "}"
        resp = sympy.Symbol(lhs + rhs)
        self.logger(ctx, resp)
        return resp

    def visitVar_underscore_var(self, ctx: ExprParser.Var_underscore_varContext):
        # rewrite x_a -> x_{a}
        lhs = ctx.getChild(0).getText() + ctx.getChild(1).getText()
        rhs = "{" + ctx.getChild(2).getText() + "}"
        resp = sympy.Symbol(lhs + rhs)
        self.logger(ctx, resp)
        return resp

    def visitVar_v(self, ctx: ExprParser.Var_vContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVar_var(self, ctx: ExprParser.Var_varContext):
        lhs = self.visit(ctx.var(0))
        rhs = self.visit(ctx.var(1))
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitVar_w(self, ctx: ExprParser.Var_wContext):
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

    def visitVariable(self, ctx: ExprParser.VariableContext):
        resp = self.visit(ctx.var())
        self.logger(ctx, resp)
        return resp

    def visitVec(self, ctx: ExprParser.VecContext):
        return self.visitChildren(ctx)


def run_test(k):
    input_stream = InputStream(k)
    lexer = ModeTagsLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = ExprParser(token_stream)
    tree = parser.prog()
    # print(tree.toStringTree(recog=parser))
    calc = Calc()
    calc.visit(tree)
    return calc.parse_tree


ok = []
failed = []
exceptions = []
no_output = []
debug = True
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
set_trace()
print(failed)
