cp ExprVisitor.py  expr_visitor.bkf
export CLASSPATH=".:/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH"
java -jar /usr/local/lib/antlr-4.11.1-complete.jar Expr.g4 -atn -long-messages -no-listener -visitor -Dlanguage=Python3
diff ExprVisitor.py expr_visitor.bkf|grep def |grep '<' |xargs -i echo '{}'  resp = ctx.getText\(\) >> test.py 

#mkdir java_gen
java -jar /usr/local/lib/antlr-4.11.1-complete.jar Expr.g4 -no-listener -visitor -Dlanguage=Java -o java_gen
cd java_gen
javac *.java
