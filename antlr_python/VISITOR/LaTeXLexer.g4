//Referenced antlr/grammars-v4/calculator.g4

lexer grammar LaTeXLexer;

VARIABLE
   : 'a'
| '\\alpha'
|'b'
|'c'
|'d'
|'i'
|'j'
|'k'
|'K'
|'l'
|'L'
|'m'
|'M'
|'n'
|'N'
|'p'
|'r'
|'t'
|'T'
|'x'
|'y'
|'z'
   ;

BEGIN_EQUATION
    : '\\begin{equation}'
    ;
END_EQUATION
    : '\\end{equation}'
    ;
POS_INFTY
    : '+' '\\infty'
    ;

NEG_INFTY:
    : '-' '\\infty'
    ;

INFTY
    : '\\infty'
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

SUP
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

