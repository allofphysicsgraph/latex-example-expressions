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

    def visitBinaryRelationalExpression(
        self, ctx: ExprParser.BinaryRelationalExpressionContext
    ):
        lhs = self.visit(ctx.atomicExpr(0))
        rhs = self.visit(ctx.atomicExpr(1))
        op = ctx.op.text
        if op == "\\neq":
            resp = sympy.Ne(lhs, rhs, evaluate=False)
        elif op == "<":
            resp = sympy.Lt(lhs, rhs, evaluate=False)
        elif op == ">":
            resp = sympy.Gt(lhs, rhs, evaluate=False)
        elif op == "\\le" or op == "\\leq":
            resp = sympy.Le(lhs, rhs, evaluate=False)
        elif op == "\\ge" or op == "\\geq":
            resp = sympy.Ge(lhs, rhs, evaluate=False)
        elif op == "=":
            resp = sympy.Eq(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitParensParens(self, ctx: ExprParser.ParensParensContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitParenthesizedExpression(
        self, ctx: ExprParser.ParenthesizedExpressionContext
    ):
        resp = self.visit(ctx.expr())
        self.logger(ctx, resp)
        return resp

    def visitIntegerVariable(self, ctx: ExprParser.IntegerVariableContext):
        lhs = int(ctx.INT().getText())
        rhs = self.visit(ctx.var())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitFunctionCallExpression(
        self, ctx: ExprParser.FunctionCallExpressionContext
    ):
        func_name = ctx.var().getText()
        args = (
            [self.visit(arg) for arg in ctx.exprList().expr()] if ctx.exprList() else []
        )
        resp = sympy.Function(func_name)(*args, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitVarParens(self, ctx: ExprParser.VarParensContext):
        lhs = self.visit(ctx.var())
        rhs = self.visit(ctx.expr())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitVarK(self, ctx: ExprParser.VarKContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarG(self, ctx: ExprParser.VarGContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarA(self, ctx: ExprParser.VarAContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarB(self, ctx: ExprParser.VarBContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarC(self, ctx: ExprParser.VarCContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarX(self, ctx: ExprParser.VarXContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarY(self, ctx: ExprParser.VarYContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarZ(self, ctx: ExprParser.VarZContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarU(self, ctx: ExprParser.VarUContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarV(self, ctx: ExprParser.VarVContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarW(self, ctx: ExprParser.VarWContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarN(self, ctx: ExprParser.VarNContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarH(self, ctx: ExprParser.VarHContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarSmallK(self, ctx: ExprParser.VarSmallKContext):
        resp = ctx.getText()
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarAlpha(self, ctx: ExprParser.VarAlphaContext):
        resp = ctx.getText()
        resp = re.sub(r"\\+", "", resp)
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitVarTheta(self, ctx: ExprParser.VarThetaContext):
        resp = ctx.getText()
        resp = re.sub(r"\\+", "", resp)
        resp = sympy.Symbol(resp)
        self.logger(ctx, resp)
        return resp

    def visitIntegerLiteral(self, ctx: ExprParser.IntegerLiteralContext):
        resp = int(ctx.INT().getText())
        self.logger(ctx, resp)
        return resp

    def visitAdditiveExpression(self, ctx: ExprParser.AdditiveExpressionContext):
        pass
        lhs = self.visit(ctx.term(0))
        # for i in range(1, len(ctx.term()):
        #    rhs = self.visit(ctx.term(i))
        #    if ctx.op[i - 1].text == "+":
        #        lhs = sympy.Add(lhs, rhs, evaluate=False)
        #    elif ctx.op[i - 1].text == "-":
        #        lhs = sympy.Add(lhs, -1 * rhs, evaluate=False)
        self.logger(ctx, lhs)
        return lhs

    def visitBracesExpression(self, ctx: ExprParser.BracesExpressionContext):
        resp = self.visit(ctx.expr())
        self.logger(ctx, resp)
        return resp

    def visitBracketedExpression(self, ctx: ExprParser.BracketedExpressionContext):
        resp = self.visit(ctx.expr())
        self.logger(ctx, resp)
        return resp

    def visitFloatLiteral(self, ctx: ExprParser.FloatLiteralContext):
        resp = ctx.FLOAT().getText()
        l = re.findall("(\..*)", resp)
        if l:
            rnd = len(list(l[0]))
            resp = sympy.Float(resp, rnd)
            self.logger(ctx, resp)
            return resp

    def visitParensVar(self, ctx: ExprParser.ParensVarContext):
        lhs = self.visit(ctx.expr())
        rhs = self.visit(ctx.var())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitBracesVar(self, ctx: ExprParser.BracesVarContext):
        lhs = self.visit(ctx.expr())
        rhs = self.visit(ctx.var())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitBracketsVarPost(self, ctx: ExprParser.BracketsVarPostContext):
        lhs = self.visit(ctx.expr())
        rhs = self.visit(ctx.var())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitBracketsVarPre(self, ctx: ExprParser.BracketsVarPreContext):
        lhs = self.visit(ctx.var())
        rhs = self.visit(ctx.expr())
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitBinomialExpression(self, ctx: ExprParser.BinomialExpressionContext):
        lhs = self.visit(ctx.numerator())
        rhs = self.visit(ctx.denominator())
        resp = sympy.binomial(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitVariableVariable(self, ctx: ExprParser.VariableVariableContext):
        lhs = self.visit(ctx.var(0))
        rhs = self.visit(ctx.var(1))
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitVariable(self, ctx: ExprParser.VariableContext):
        resp = sympy.Symbol(ctx.getText())
        self.logger(ctx, resp)
        return resp

    def visitFloatVariable(self, ctx: ExprParser.FloatVariableContext):
        lhs_text = ctx.FLOAT().getText()
        rhs = self.visit(ctx.var())
        l = re.findall("(\..*)", lhs_text)
        lhs = sympy.Float(
            lhs_text, len(l[0]) if l else 15
        )  # Default precision if no decimal
        resp = sympy.Mul(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitMultiplicativeExpression(
        self, ctx: ExprParser.MultiplicativeExpressionContext
    ):
        lhs = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            rhs = self.visit(ctx.factor(i))
            op = ctx.op[i - 1].text
            if op in ("*", "\\cdot", "\\times"):
                lhs = sympy.Mul(lhs, rhs, evaluate=False)
            elif op in ("/", "\\div"):
                lhs = sympy.Mul(lhs, sympy.Pow(rhs, -1, evaluate=False), evaluate=False)
        self.logger(ctx, lhs)
        return lhs

    def visitSymbolLiteral(self, ctx: ExprParser.SymbolLiteralContext):
        resp = sympy.Symbol(ctx.getText())
        self.logger(ctx, resp)
        return resp

    def visitAbsExpression(self, ctx: ExprParser.AbsExpressionContext):
        resp = self.visit(ctx.expr())
        resp = sympy.Abs(resp, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitFractionExpression(self, ctx: ExprParser.FractionExpressionContext):
        num = self.visit(ctx.numerator())
        den = self.visit(ctx.denominator())
        resp = sympy.Mul(num, sympy.Pow(den, -1, evaluate=False), evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitVec(self, ctx: ExprParser.VecContext):
        resp = sympy.physics.vector.Vector(
            ctx.group().getText()
        )  # Consider a better representation
        self.logger(ctx, resp)
        return resp

    def visitHat(self, ctx: ExprParser.HatContext):
        resp = sympy.Symbol(
            ctx.group().getText() + "_hat"
        )  # Or a better way to represent hats
        self.logger(ctx, resp)
        return resp

    def visitOverline(self, ctx: ExprParser.OverlineContext):
        resp = sympy.Symbol(
            "overline_{" + ctx.group().getText() + "}"
        )  # Or a better representation
        self.logger(ctx, resp)
        return resp

    def visitIntegral(self, ctx: ExprParser.IntegralContext):
        expr = self.visit(ctx.expr())
        var = sympy.Symbol(ctx.var().text)
        resp = sympy.Integral(expr, var, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitFactorial(self, ctx: ExprParser.FactorialContext):
        resp = self.visit(ctx.atomicExpr())
        resp = sympy.factorial(resp, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitLogBase(self, ctx: ExprParser.LogBaseContext):
        base = self.visit(ctx.subSupArgument().group().expr())
        arg = self.visit(ctx.argument())
        resp = sympy.log(arg, base, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitLimit(self, ctx: ExprParser.LimitContext):
        var = sympy.Symbol(ctx.group().expr().getText())
        target = self.visit(ctx.expr(0))
        expr = self.visit(ctx.expr(1))
        direction = "+-"
        if ctx.PLUS():
            direction = "+"
        if ctx.MINUS():
            direction = "-"
        resp = sympy.Limit(expr, var, target, dir=direction)
        self.logger(ctx, resp)
        return resp

    def visitLg(self, ctx: ExprParser.LgContext):
        expr = self.visit(ctx.argument())
        resp = sympy.log(expr, 10, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitExp(self, ctx: ExprParser.ExpContext):
        expr = self.visit(ctx.argument())
        resp = sympy.exp(expr)
        self.logger(ctx, resp)
        return resp

    def visitLn(self, ctx: ExprParser.LnContext):
        from sympy.core.numbers import E

        expr = self.visit(ctx.argument())
        resp = sympy.log(expr, E, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitFloor(self, ctx: ExprParser.FloorContext):
        resp = self.visit(ctx.argument())
        resp = sympy.floor(resp, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitCeiling(self, ctx: ExprParser.CeilingContext):
        resp = self.visit(ctx.argument())
        resp = sympy.ceiling(resp, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitSin(self, ctx: ExprParser.SinContext):
        argument = self.visit(ctx.argument())
        resp = sympy.sin(argument)
        self.logger(ctx, resp)
        return resp

    def visitArccos(self, ctx: ExprParser.ArccosContext):
        argument = self.visit(ctx.argument())
        resp = sympy.acos(argument)
        self.logger(ctx, resp)
        return resp

    def visitArccot(self, ctx: ExprParser.ArccotContext):
        argument = self.visit(ctx.argument())
        resp = sympy.acot(argument)
        self.logger(ctx, resp)
        return resp

    def visitArccsc(self, ctx: ExprParser.ArccscContext):
        argument = self.visit(ctx.argument())
        resp = sympy.acsc(argument)
        self.logger(ctx, resp)
        return resp

    def visitArcosh(self, ctx: ExprParser.ArcoshContext):
        argument = self.visit(ctx.argument())
        resp = sympy.acosh(argument)
        self.logger(ctx, resp)
        return resp

    def visitArcsec(self, ctx: ExprParser.ArcsecContext):
        argument = self.visit(ctx.argument())
        resp = sympy.asec(argument)
        self.logger(ctx, resp)
        return resp

    def visitArcsin(self, ctx: ExprParser.ArcsinContext):
        argument = self.visit(ctx.argument())
        resp = sympy.asin(argument)
        self.logger(ctx, resp)
        return resp

    def visitArctan(self, ctx: ExprParser.ArctanContext):
        argument = self.visit(ctx.argument())
        resp = sympy.atan(argument)
        self.logger(ctx, resp)
        return resp

    def visitArsinh(self, ctx: ExprParser.ArsinhContext):
        argument = self.visit(ctx.argument())
        resp = sympy.asinh(argument)
        self.logger(ctx, resp)
        return resp

    def visitArtanh(self, ctx: ExprParser.ArtanhContext):
        argument = self.visit(ctx.argument())
        resp = sympy.atanh(argument)
        self.logger(ctx, resp)
        return resp

    def visitCos(self, ctx: ExprParser.CosContext):
        argument = self.visit(ctx.argument())
        resp = sympy.cos(argument)
        self.logger(ctx, resp)
        return resp

    def visitCosh(self, ctx: ExprParser.CoshContext):
        argument = self.visit(ctx.argument())
        resp = sympy.cosh(argument)
        self.logger(ctx, resp)
        return resp

    def visitCot(self, ctx: ExprParser.CotContext):
        argument = self.visit(ctx.argument())
        resp = sympy.cot(argument)
        self.logger(ctx, resp)
        return resp

    def visitCsc(self, ctx: ExprParser.CscContext):
        argument = self.visit(ctx.argument())
        resp = sympy.csc(argument)
        self.logger(ctx, resp)
        return resp

    def visitSec(self, ctx: ExprParser.SecContext):
        argument = self.visit(ctx.argument())
        resp = sympy.sec(argument)
        self.logger(ctx, resp)
        return resp

    def visitSinh(self, ctx: ExprParser.SinhContext):
        argument = self.visit(ctx.argument())
        resp = sympy.sinh(argument)
        self.logger(ctx, resp)
        return resp

    def visitTanh(self, ctx: ExprParser.TanhContext):
        argument = self.visit(ctx.argument())
        resp = sympy.tanh(argument)
        self.logger(ctx, resp)
        return resp

    def visitTan(self, ctx: ExprParser.TanContext):
        argument = self.visit(ctx.argument())
        resp = sympy.tan(argument)
        self.logger(ctx, resp)
        return resp

    def visitAtom(self, ctx: ExprParser.AtomContext):
        return self.visitChildren(ctx)

    def visitNumeratorInteger(self, ctx: ExprParser.NumeratorIntegerContext):
        resp = int(ctx.getText())
        self.logger(ctx, resp)
        return resp

    def visitNumeratorExpr(self, ctx: ExprParser.NumeratorExprContext):
        resp = self.visit(ctx.group().expr())
        self.logger(ctx, resp)
        return resp

    def visitDenominatorInteger(self, ctx: ExprParser.DenominatorIntegerContext):
        resp = int(ctx.getText())
        self.logger(ctx, resp)
        return resp

    def visitDenominatorExpr(self, ctx: ExprParser.DenominatorExprContext):
        resp = self.visit(ctx.group().expr())
        self.logger(ctx, resp)
        return resp

    def visitEquation(self, ctx: ExprParser.EquationContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        resp = sympy.Eq(lhs, rhs, evaluate=False)
        self.logger(ctx, resp)
        return resp

    def visitVarSubscriptVar(self, ctx: ExprParser.VarSubscriptVarContext):
        base = self.visit(ctx.var())
        subscript = self.visit(ctx.groupVar().var())
        resp = sympy.Symbol(f"{base}_{{{subscript}}}")
        self.logger(ctx, resp)
        return resp

    def visitVarSubscriptInt(self, ctx: ExprParser.VarSubscriptIntContext):
        base = self.visit(ctx.var())
        subscript = ctx.INT().getText()
        resp = sympy.Symbol(f"{base}_{subscript}")
        self.logger(ctx, resp)
        return resp

    def visitGroupVar(self, ctx: ExprParser.GroupVarContext):
        return self.visit(ctx.var())

    def visitSymbolLiteral(self, ctx: ExprParser.SymbolLiteralContext):
        resp = sympy.Symbol(ctx.getText())
        self.logger(ctx, resp)
        return resp

    def visitVar(self, ctx: ExprParser.VarContext):
        return ctx.getText()

    def visitExpressionStatement(self, ctx: ExprParser.ExpressionStatementContext):
        return self.visit(ctx.expr())

    def visitEquationStatement(self, ctx: ExprParser.EquationStatementContext):
        return self.visit(ctx.equation())

    def visitGroup(self, ctx: ExprParser.GroupContext):
        return self.visit(ctx.expr())


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
    100 * len(ok) / ix if ix > 0 else 0,
)
set_trace()
print(failed)
