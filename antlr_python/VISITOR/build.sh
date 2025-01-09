export CLASSPATH=".:/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH"
java -jar /usr/local/lib/antlr-4.11.1-complete.jar ExprLexer.g4 -atn -long-messages  -Xforce-atn -no-listener -visitor -Dlanguage=Python3
java -jar /usr/local/lib/antlr-4.11.1-complete.jar ExprParser.g4 -atn -long-messages  -Xforce-atn -no-listener -visitor -Dlanguage=Python3

#mkdir java_gen
#java -jar /usr/local/lib/antlr-4.11.1-complete.jar Expr.g4 -no-listener -visitor -Dlanguage=Java -o java_gen
#cd java_gen
#javac *.java
