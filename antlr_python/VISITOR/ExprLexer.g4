lexer grammar ExprLexer;

HBAR
   : '\\hbar'
   ;

HAT
   : '\\hat'
   ;

LOG
   : '\\log'
   ;

LG
   : '\\lg'
   ;

EXP
   : '\\exp'
   ;

LN
   : '\\ln'
   ;

PRIME
   : '\''
   ;

RFLOOR
   : '\\rfloor'
   ;

LFLOOR
   : '\\lfloor'
   ;

ADD
   : '+'
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

EQUALS
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

FLOAT
   : INT? ('.' [0-9]+)
   | '-' INT? ('.' [0-9]+)
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

FRAC_INT_INT
   : ('\\frac' | '\\tfrac' | '\\dfrac') SINGLE_DIGIT NON_ZERO_DIGIT
   ;

FRAC
   : ('\\frac' | '\\tfrac' | '\\dfrac')
   ;

fragment SINGLE_DIGIT
   : [0-9]
   ;

fragment NON_ZERO_DIGIT
   : [1-9]
   ;

INT
   : SINGLE_DIGIT
   | NON_ZERO_DIGIT SINGLE_DIGIT+
   ;

