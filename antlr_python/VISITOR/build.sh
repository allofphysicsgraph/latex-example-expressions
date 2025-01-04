cp ExprVisitor.py  expr_visitor.bkf
export CLASSPATH=".:/usr/local/lib/antlr-4.13.1-complete.jar:$CLASSPATH"
java -jar /usr/local/lib/antlr-4.13.1-complete.jar Expr.g4 -no-listener -visitor -Dlanguage=Python3
diff ExprVisitor.py expr_visitor.bkf|grep def |grep '<' |xargs -i echo '{}':  pass
