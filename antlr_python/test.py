import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from LATEXLexer import LATEXLexer
from LATEXParser import LATEXParser


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
        print(input_stream)
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = LATEXLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    for tk in token_stream.tokens:
        print(tk)

    parser = LATEXParser(token_stream)
    tree = parser.words()
    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)
