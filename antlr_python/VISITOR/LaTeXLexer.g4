//Referenced antlr/grammars-v4/calculator.g4

lexer grammar LaTeXLexer;

VARIABLE
   : 'a'
   | 'b'
   | 'c'
   | 'x'
   | 'y'
   | 'z'
   | 'k'
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

POW
   : '^'
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
SUM:
    '\\sum'
    ;
SUB:
    '_'
    ;


FLOAT
   : INTEGER? ('.' INTEGER)
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

