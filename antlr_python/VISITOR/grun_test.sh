#!/bin/bash
export CLASSPATH=".:/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH"
antlr4='java -jar /usr/local/lib/antlr-4.11.1-complete.jar'
grun='java org.antlr.v4.runtime.misc.TestRig' 

$antlr4 LaTeXLexer.g4 LaTeXParser.g4
javac *.java
$grun LaTeX prog "$1" -gui
