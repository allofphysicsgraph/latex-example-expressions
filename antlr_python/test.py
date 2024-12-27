import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from LaTeXLexer import LaTeXLexer
from LaTeXParser import LaTeXParser
from LaTeXListener import LaTeXListener
from collections import defaultdict
from pudb import set_trace
import sympy


class SympyEmitter(LaTeXListener):
    def __init__(self):
        self.sympy = defaultdict(list)
        self.results = defaultdict(list)

    def getSympy(self):
        return self.sympy

    def setSympy(self, ctx, value):
        self.sympy[ctx].append(value)

    def exitExpression_variable_sub_number(self, ctx):
        return self.setSympy("exitExpression_variable_sub_number", ctx.getText())

    def exitARCCOS(self, ctx):
        return self.setSympy("exitARCCOS", ctx.getText())

    def exitARCCOT(self, ctx):
        return self.setSympy("exitARCCOT", ctx.getText())

    def exitARCCSC(self, ctx):
        return self.setSympy("exitARCCSC", ctx.getText())

    def exitARCOSH(self, ctx):
        return self.setSympy("exitARCOSH", ctx.getText())

    def exitARCSEC(self, ctx):
        return self.setSympy("exitARCSEC", ctx.getText())

    def exitARCSIN(self, ctx):
        return self.setSympy("exitARCSIN", ctx.getText())

    def exitARCTAN(self, ctx):
        return self.setSympy("exitARCTAN", ctx.getText())

    def exitARSINH(self, ctx):
        return self.setSympy("exitARSINH", ctx.getText())

    def exitARTANH(self, ctx):
        return self.setSympy("exitARTANH", ctx.getText())

    def exitAtom(self, ctx):
        return self.setSympy("exitAtom", ctx.getText())

    def exitCOSH(self, ctx):
        return self.setSympy("exitCOSH", ctx.getText())

    def exitCOS(self, ctx):
        return self.setSympy("exitCOS", ctx.getText())

    def exitCOT(self, ctx):
        return self.setSympy("exitCOT", ctx.getText())

    def exitCSC(self, ctx):
        return self.setSympy("exitCSC", ctx.getText())

    def exitExpression_EQUAL_expression(self, ctx):
        return self.setSympy("exitExpression_EQUAL_expression", ctx.getText())

    def exitExpression_GTE_expression(self, ctx):
        return self.setSympy("exitExpression_GTE_expression", ctx.getText())

    def exitExpression_GT_expression(self, ctx):
        return self.setSympy("exitExpression_GT_expression", ctx.getText())

    def exitExpression_LTE_expression(self, ctx):
        return self.setSympy("exitExpression_LTE_expression", ctx.getText())

    def exitExpression_LT_expression(self, ctx):
        return self.setSympy("exitExpression_LT_expression", ctx.getText())

    def exitExpression_NEQ_expression(self, ctx):
        return self.setSympy("exitExpression_NEQ_expression", ctx.getText())

    def exitExpression_number_variable(self, ctx):
        return self.setSympy("exitExpression_number_variable", ctx.getText())

    def exitExpression_variable(self, ctx):
        return self.setSympy("exitExpression_variable", ctx.getText())

    def exitEXP(self, ctx):
        return self.setSympy("exitEXP", ctx.getText())

    def exitLG(self, ctx):
        return self.setSympy("exitLG", ctx.getText())

    def exitLN(self, ctx):
        return self.setSympy("exitLN", ctx.getText())

    def exitLOG(self, ctx):
        return self.setSympy("exitLOG", ctx.getText())

    def exitMath(self, ctx):
        return self.setSympy("exitMath", ctx.getText())

    def exitMulDiv(self, ctx):
        return self.setSympy("exitMulDiv", ctx.getText())

    def exitMult(self, ctx):
        return self.setSympy("exitMult", ctx.getText())

    def exitNm(self, ctx):
        return self.setSympy("exitNm", ctx.getText())

    def exitNumber(self, ctx):
        return self.setSympy("exitNumber", ctx.getText())

    def exitParenthesis(self, ctx):
        return self.setSympy("exitParenthesis", ctx.getText())

    def exitPow(self, ctx):
        return self.setSympy("exitPow", ctx.getText())

    def exitSEC(self, ctx):
        return self.setSympy("exitSEC", ctx.getText())

    def exitSINH(self, ctx):
        return self.setSympy("exitSINH", ctx.getText())

    def exitSIN(self, ctx):
        return self.setSympy("exitSIN", ctx.getText())

    def exitTANH(self, ctx):
        return self.setSympy("exitTANH", ctx.getText())

    def exitTAN(self, ctx):
        return self.setSympy("exitTAN", ctx.getText())

    def exitUnaryPlus(self, ctx):
        return self.setSympy("exitUnaryPlus", ctx.getText())

    def exitUnary(self, ctx):
        return self.setSympy("exitUnary", ctx.getText())

    def exitVariable(self, ctx):
        return self.setSympy("exitVariable", ctx.getText())

    def exitEQTN(self, ctx):
        return self.setSympy("exitEQTN", ctx.getText())

    def exitMath(self, ctx):
        return self.setSympy("exitMath", ctx.getText())

    def exitExpression_GT_expression(self, ctx):
        return self.setSympy("exitExpression_GT_expression", ctx.getText())

    def enterAddition(self, ctx: LaTeXParser.AdditionContext):
        print(ctx.getChildCount())

    def exitAddition(self, ctx: LaTeXParser.AdditionContext):
        print(ctx.getChildCount())
        lh = sympy.Number(ctx.expression(0).getText())
        rh = sympy.Number(ctx.expression(1).getText())
        self.setSympy("exitAddition", ctx.getText())
        self.results['expressions'].append(sympy.Add(lh, rh, evaluate=False))
        print(self.results)
        return self.setSympy("exitAddition", ctx.getText())

    # def enterAddition(self,ctx): print(ctx.op.text,ctx.expression(0).getText(),ctx.expression(1).getText())
    def exitMulDiv(self, ctx):
        return self.setSympy("exitMulDiv", ctx.getText())

    def exitEQTN(self, ctx):
        return self.setSympy("exitEQTN", ctx.getText())

    def exitExpression_LTE_expression(self, ctx):
        return self.setSympy("exitExpression_LTE_expression", ctx.getText())

    def exitUnaryPlus(self, ctx):
        return self.setSympy("exitUnaryPlus", ctx.getText())

    def exitExpression_variable_sub_number(self, ctx):
        return self.setSympy("exitExpression_variable_sub_number", ctx.getText())

    def exitExpression_NEQ_expression(self, ctx):
        return self.setSympy("exitExpression_NEQ_expression", ctx.getText())

    def exitUnary(self, ctx):
        return self.setSympy("exitUnary", ctx.getText())

    def exitExpression_variable(self, ctx):
        return self.setSympy("exitExpression_variable", ctx.getText())

    def exitParenthesis(self, ctx):
        return self.setSympy("exitParenthesis", ctx.getText())

    def exitSubtraction(self, ctx):
        return self.setSympy("exitSubtraction", ctx.getText())

    def exitMult(self, ctx):
        return self.setSympy("exitMult", ctx.getText())

    def exitExpression_GTE_expression(self, ctx):
        return self.setSympy("exitExpression_GTE_expression", ctx.getText())

    def exitExpression_EQUAL_expression(self, ctx):
        return self.setSympy("exitExpression_EQUAL_expression", ctx.getText())

    def exitExpression_number_variable(self, ctx):
        return self.setSympy("exitExpression_number_variable", ctx.getText())

    def exitPow(self, ctx):
        return self.setSympy("exitPow", ctx.getText())

    def exitExpression_LT_expression(self, ctx):
        return self.setSympy("exitExpression_LT_expression", ctx.getText())

    def exitNm(self, ctx):
        return self.setSympy("exitNm", int(ctx.getText()))

    def exitEquation(self, ctx):
        return self.setSympy("exitEquation", ctx.getText())

    def exitVariable(self, ctx):
        return self.setSympy("exitVariable", ctx.getText())

    def exitNumber(self, ctx):
        return self.setSympy("exitNumber", ctx.getText())

    def exitAtom(self, ctx):
        return self.setSympy("exitAtom", ctx.getText())

    def exitTAN(self, ctx):
        return self.setSympy("exitTAN", ctx.getText())

    def exitTANH(self, ctx):
        return self.setSympy("exitTANH", ctx.getText())

    def exitARCTAN(self, ctx):
        return self.setSympy("exitARCTAN", ctx.getText())

    def exitLN(self, ctx):
        return self.setSympy("exitLN", ctx.getText())

    def exitLOG(self, ctx):
        return self.setSympy("exitLOG", ctx.getText())

    def exitCOS(self, ctx):
        return self.setSympy("exitCOS", ctx.getText())

    def exitARCSIN(self, ctx):
        return self.setSympy("exitARCSIN", ctx.getText())

    def exitCOT(self, ctx):
        return self.setSympy("exitCOT", ctx.getText())

    def exitARTANH(self, ctx):
        return self.setSympy("exitARTANH", ctx.getText())

    def exitARCCSC(self, ctx):
        return self.setSympy("exitARCCSC", ctx.getText())

    def exitSEC(self, ctx):
        return self.setSympy("exitSEC", ctx.getText())

    def exitARCSEC(self, ctx):
        return self.setSympy("exitARCSEC", ctx.getText())

    def exitCSC(self, ctx):
        return self.setSympy("exitCSC", ctx.getText())

    def exitARSINH(self, ctx):
        return self.setSympy("exitARSINH", ctx.getText())

    def exitSINH(self, ctx):
        return self.setSympy("exitSINH", ctx.getText())

    def exitARCCOT(self, ctx):
        return self.setSympy("exitARCCOT", ctx.getText())

    def exitSIN(self, ctx):
        return self.setSympy("exitSIN", ctx.getText())

    def exitLG(self, ctx):
        return self.setSympy("exitLG", ctx.getText())

    def exitARCCOS(self, ctx):
        return self.setSympy("exitARCCOS", ctx.getText())

    def exitEXP(self, ctx):
        return self.setSympy("exitEXP", ctx.getText())

    def exitARCOSH(self, ctx):
        return self.setSympy("exitARCOSH", ctx.getText())

    def exitCOSH(self, ctx):
        return self.setSympy("exitCOSH", ctx.getText())


# from https://github.com/antlr/antlr4/blob/master/runtime/Python3/bin/pygrun
# this is a python version of TestRig
def beautify_lisp_string(in_string):
    indent_size = 3
    add_indent = " " * indent_size
    out_string = in_string[0]  # no indent for 1st (
    indent = ""
    for i in range(1, len(in_string)):
        if in_string[i] == "(" and in_string[i + 1] != " ":
            indent += add_indent
            out_string += "\n" + indent + "("
        elif in_string[i] == ")":
            out_string += ")"
            if len(indent) > 0:
                indent = indent.replace(add_indent, "", 1)
        else:
            out_string += in_string[i]
    return out_string


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
        print(input_stream)
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = LaTeXLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    # token_stream.fill()
    # for tk in token_stream.tokens:
    #    print(tk)

    parser = LaTeXParser(token_stream)
    from pudb import set_trace

    parser.buildParseTrees = True
    tree = parser.math()
    # set_trace()
    # print(tree.toStringTree(parser))
    # tree = parser.math()
    # set_trace()
    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)
    listener = SympyEmitter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    print(listener.getSympy())
    # print(beautify_lisp_string(lisp_tree_str))
