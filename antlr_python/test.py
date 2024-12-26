import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from LaTeXLexer import LaTeXLexer
from LaTeXParser import LaTeXParser
from LaTeXListener import LaTeXListener
from collections import defaultdict


class SympyEmitter(LaTeXListener):
    def __init__(self):
        self.sympy = defaultdict(list)

    def getSympy(self):
        return self.sympy

    def setSympy(self, ctx, value):
        self.sympy[ctx].append(value)

    def exitMath(self, ctx):
        return self.setSympy("exitMath", ctx.getText())

    def exitRelation(self, ctx):
        return self.setSympy("exitRelation", ctx.getText())

    def exitEquality(self, ctx):
        return self.setSympy("exitEquality", ctx.getText())

    def exitExpr(self, ctx):
        return self.setSympy("exitExpr", ctx.getText())

    def exitAdditive(self, ctx):
        return self.setSympy("exitAdditive", ctx.getText())

    def exitMp(self, ctx):
        return self.setSympy("exitMp", ctx.getText())

    def exitMp_nofunc(self, ctx):
        return self.setSympy("exitMp_nofunc", ctx.getText())

    def exitUnary(self, ctx):
        return self.setSympy("exitUnary", ctx.getText())

    def exitUnary_nofunc(self, ctx):
        return self.setSympy("exitUnary_nofunc", ctx.getText())

    def exitPostfix(self, ctx):
        return self.setSympy("exitPostfix", ctx.getText())

    def exitPostfix_nofunc(self, ctx):
        return self.setSympy("exitPostfix_nofunc", ctx.getText())

    def exitPostfix_op(self, ctx):
        return self.setSympy("exitPostfix_op", ctx.getText())

    def exitEval_at(self, ctx):
        return self.setSympy("exitEval_at", ctx.getText())

    def exitEval_at_sub(self, ctx):
        return self.setSympy("exitEval_at_sub", ctx.getText())

    def exitEval_at_sup(self, ctx):
        return self.setSympy("exitEval_at_sup", ctx.getText())

    def exitExp(self, ctx):
        return self.setSympy("exitExp", ctx.getText())

    def exitExp_nofunc(self, ctx):
        return self.setSympy("exitExp_nofunc", ctx.getText())

    def exitComp(self, ctx):
        return self.setSympy("exitComp", ctx.getText())

    def exitComp_nofunc(self, ctx):
        return self.setSympy("exitComp_nofunc", ctx.getText())

    def exitGroup(self, ctx):
        return self.setSympy("exitGroup", ctx.getText())

    def exitAbs_group(self, ctx):
        return self.setSympy("exitAbs_group", ctx.getText())

    def exitNumber(self, ctx):
        return self.setSympy("exitNumber", ctx.getText())

    def exitAtom(self, ctx):
        return self.setSympy("exitAtom", ctx.getText())

    def exitBra(self, ctx):
        return self.setSympy("exitBra", ctx.getText())

    def exitKet(self, ctx):
        return self.setSympy("exitKet", ctx.getText())

    def exitMathit(self, ctx):
        return self.setSympy("exitMathit", ctx.getText())

    def exitMathit_text(self, ctx):
        return self.setSympy("exitMathit_text", ctx.getText())

    def exitFrac(self, ctx):
        return self.setSympy("exitFrac", ctx.getText())

    def exitBinom(self, ctx):
        return self.setSympy("exitBinom", ctx.getText())

    def exitFloor(self, ctx):
        return self.setSympy("exitFloor", ctx.getText())

    def exitCeil(self, ctx):
        return self.setSympy("exitCeil", ctx.getText())

    def exitFunc_normal(self, ctx):
        return self.setSympy("exitFunc_normal", ctx.getText())

    def exitFunc(self, ctx):
        return self.setSympy("exitFunc", ctx.getText())

    def exitArgs(self, ctx):
        return self.setSympy("exitArgs", ctx.getText())

    def exitLimit_sub(self, ctx):
        return self.setSympy("exitLimit_sub", ctx.getText())

    def exitFunc_arg(self, ctx):
        return self.setSympy("exitFunc_arg", ctx.getText())

    def exitFunc_arg_noparens(self, ctx):
        return self.setSympy("exitFunc_arg_noparens", ctx.getText())

    def exitSubexpr(self, ctx):
        return self.setSympy("exitSubexpr", ctx.getText())

    def exitSupexpr(self, ctx):
        return self.setSympy("exitSupexpr", ctx.getText())

    def exitSubeq(self, ctx):
        return self.setSympy("exitSubeq", ctx.getText())

    def exitSupeq(self, ctx):
        return self.setSympy("exitSupeq", ctx.getText())


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
    token_stream.fill()
    for tk in token_stream.tokens:
        print(tk)

    parser = LaTeXParser(token_stream)
    tree = parser.math()
    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)
    listener = SympyEmitter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    print(listener.getSympy())
    # print(beautify_lisp_string(lisp_tree_str))
