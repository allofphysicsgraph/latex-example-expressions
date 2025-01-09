lexer grammar ExprLexer;

ADD
   : '+'
   ;

BINOM
   : '\\binom'
   ;

CDOT
   : '\\cdot'
   ;

COLON
   : ':'
   ;

COMMA
   : ','
   ;

DIV
   : '/'
   | '\\div'
   ;

DOLLAR_SIGN
   : '$'
   ;

FUNC_INT
   : '\\int'
   ;

LB
   : '{'
   ;

LIM
   : '\\lim'
   ;

MUL
   : '*'
   ;

PROD
   : '\\prod'
   ;

RB
   : '}'
   ;

SQRT
   : '\\sqrt'
   ;

SUM
   : '\\sum'
   ;

TIMES
   : '\\times'
   ;

LBR
   : '['
   ;

RBR
   : ']'
   ;

MINUS
   : '-'
   ;

EQUAL
   : '='
   | '=='
   | '\\equiv'
   ;

LT
   : '<'
   ;

LTE
   : '\\leq'
   | '\\le'
   | '\\leqslant'
   ;

GT
   : '>'
   ;

GTE
   : '\\geq'
   | '\\ge'
   | '\\geqslant'
   ;

UNEQUAL
   : '!='
   | '!=='
   | '\\ne'
   | '\\neq'
   | '\\not\\equiv'
   ;

LP
   : '('
   ;

RP
   : ')'
   ;

INT
   : '0'
   | [1-9] [0-9]*
   ;

FLOAT
   : INT? ('.' [0-9]+)
   | '-' INT? ('.' [0-9]+)
   ;

PRIME
   : '\''
   ;

BEGIN_EQ
   : '\\begin{equation}' -> skip
   ;

END_EQ
   : '\\end{equation}' -> skip
   ;

IGNORE
   : ('\\left\\' | '\\right\\' | '\\!' | '\\;' | '\\:' | '\\quad' | '\\qquad' | '\\thickspace' | '\\,' | '\\negthickspace' | '\\displaystyle' | '\\left' | '\\right' | '\\begin{align}' | '\\end{align}' | '\\negmedspace' | '\\medspace' | '\\negthinspace' | '\\thinspace') -> skip
   ;

NEWLINE
   : '\n' -> skip
   ;

WS
   : [ \t]+ -> skip
   ;

ALPHA
   : '\\alpha'
   ;

BETA
   : '\\beta'
   ;

THETA
   : '\\theta'
   ;

PI
   : '\\pi'
   ;

SUB
   : '_'
   ;

SUP
   : '^'
   ;

K_U_VAR
   : 'K'
   ;

G_U_VAR
   : 'G'
   ;

X_VAR
   : 'x'
   ;

Y_VAR
   : 'y'
   ;

Z_VAR
   : 'z'
   ;

A_VAR
   : 'a'
   ;

B_VAR
   : 'b'
   ;

C_VAR
   : 'c'
   ;

N_VAR
   : 'n'
   ;

H_VAR
   : 'h'
   ;

K_VAR
   : 'k'
   ;

U_VAR
   : 'u'
   ;

V_VAR
   : 'v'
   ;

W_VAR
   : 'w'
   ;

SIN
   : '\\sin'
   ;

COS
   : '\\cos'
   ;

FRAC
   : '\\frac' -> mode (NUMERATOR)
   ;

mode NUMERATOR;
SINGLE_DIGIT
   : [0-9] -> mode (DENOMINATOR)
   ;

mode DENOMINATOR;
SINGLE_DIGIT_NON_ZERO
   : [1-9] -> mode (DEFAULT_MODE)
   ;

