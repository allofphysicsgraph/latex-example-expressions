export CLASSPATH=".:/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH"
java -jar /usr/local/lib/antlr-4.11.1-complete.jar ExprLexer.g4  -long-messages  -no-listener -visitor -Dlanguage=Python3
java -jar /usr/local/lib/antlr-4.11.1-complete.jar ExprParser.g4  -long-messages   -no-listener -visitor -Dlanguage=Python3

java -jar /usr/local/lib/antlr-4.11.1-complete.jar ExprLexer.g4  -long-messages  -no-listener -visitor -Dlanguage=Java
java -jar /usr/local/lib/antlr-4.11.1-complete.jar ExprParser.g4  -long-messages   -no-listener -visitor -Dlanguage=Java
javac *.java
#mkdir java_gen
#java -jar /usr/local/lib/antlr-4.11.1-complete.jar Expr.g4 -no-listener -visitor -Dlanguage=Java -o java_gen
#cd java_gen
#javac *.java
