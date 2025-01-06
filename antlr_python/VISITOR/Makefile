grammarinator:
	mkdir exprGenerator
	grammarinator-process Expr.g4 -o exprGenerator/
	mkdir test
	grammarinator-generate ExprGenerator.ExprGenerator -r prog -d 10 -o ./test/test_%d.html -n 100 -s ExprGenerator.simple_space_serializer --sys-path ./exprGenerator/
