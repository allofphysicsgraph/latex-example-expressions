//Referenced antlr/grammars-v4/calculator.g4

lexer grammar LaTeXLexer;

VARIABLE
   : 'a'
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
| GREEK
   ;

GREEK:
    '\\alpha' |
    '\\beta' |
    '\\chi' |
    '\\delta' |
    '\\Delta' |
    '\\epsilon' |
    '\\eta' |
    '\\gamma' |
    '\\Gamma' |
    '\\iota' |
    '\\kappa' |
    '\\lambda' |
    '\\Lambda' |
    '\\mu' |
    '\\nu' |
    '\\omega' |
    '\\Omega' |
    '\\omicron' |
    '\\phi' |
    '\\Phi' |
    '\\Pi' |
    '\\psi' |
    '\\Psi' |
    '\\rho' |
    '\\sigma' |
    '\\Sigma' |
    '\\tau' |
    '\\theta' |
    '\\Theta' |
    '\\upsilon' |
    '\\Upsilon' |
    '\\varepsilon' |
    '\\varphi' |
    '\\varpi' |
    '\\varrho' |
    '\\varsigma' |
    '\\vartheta' |
    '\\xi' |
    '\\Xi' |
    '\\zeta' 
    ;
LIM: 
    '\\lim' SUB LB
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

NEG_INFTY
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

RIGHTARROW:
    '\\rightarrow'
    ;
TO:
    '\\to'
    | RIGHTARROW
    ;

POS:
    SUP PLUS
    ;

NEG:
    SUP MINUS
    ;

DOWNARROW:
    '\\downarrow'
    ;

ABS_VARIABLE:
    '|' VARIABLE '|'
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

