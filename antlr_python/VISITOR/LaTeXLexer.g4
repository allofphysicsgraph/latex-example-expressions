//Referenced antlr/grammars-v4/calculator.g4

lexer grammar LaTeXLexer;

X
   : 'x'
   ;

PI
   : 'PI'
   ;

LB
   : '{'
   ;

RB
   : '}'
   ;

LP
   : '('
   ;

RP
   : ')'
   ;

LBR
   : '['
   ;

RBR
   : ']'
   ;

PLUS
   : '+'
   ;

MINUS
   : '-'
   ;

MUL
   : '*'
   ;

DIVIDE
   : '/'
   ;

EQUALS
   : '='
   ;

INTEGER
   : ZERO
   | DIGIT_NON_ZERO DIGIT*
   ;

fragment ZERO
   : '0'
   ;

fragment DIGIT_NON_ZERO
   : [1-9]
   ;

fragment DIGIT
   : ZERO
   | DIGIT_NON_ZERO
   ;

WS
   : [ \r\n\t] -> skip
   ;

