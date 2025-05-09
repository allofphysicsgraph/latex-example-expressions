export CLASSPATH=".:/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH"
java -jar /usr/local/lib/antlr-4.11.1-complete.jar FracLexer.g4  -atn -long-messages  -Xforce-atn -no-listener -visitor -Dlanguage=Python3
java -jar /usr/local/lib/antlr-4.11.1-complete.jar FracParser.g4  -atn -long-messages  -Xforce-atn -no-listener -visitor -Dlanguage=Python3

