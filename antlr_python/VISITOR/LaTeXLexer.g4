//Referenced antlr/grammars-v4/calculator.g4

lexer grammar LaTeXLexer;

VARIABLE
   : 'a'
   | 'A'
   | 'b'
   | 'B'
   | 'C'
   | 'd'
   | 'e'
   | 'E'
   | 'F'
   | 'g'
   | 'h'
   | 'H'
   | 'i'
   | 'I'
   | 'j'
   | 'J'
   | 'k'
   | 'K'
   | 'l'
   | 'L'
   | 'm'
   | 'M'
   | 'n'
   | 'N'
   | 'o'
   | 'p'
   | 'P'
   | 'q'
   | 'Q'
   | 'r'
   | 'R'
   | 's'
   | 'S'
   | 't'
   | 'T'
   | 'u'
   | 'U'
   | 'v'
   | 'V'
   | 'w'
   | 'W'
   | 'x'
   | 'y'
   | 'z'
   | 'Z'
   ;

LIM
   : '\\lim' SUB LB
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

LANGLE
   : '\\langle'
   ;

RANGLE
   : '\\rangle'
   ;

COMMA
   : ','
   ;

LT
   : '<'
   ;

NEQ
   : '\\neq'
   ;

SUM
   : '\\sum'
   ;

SUB
   : '_'
   ;

RIGHTARROW
   : '\\rightarrow'
   ;

TO
   : '\\to'
   | RIGHTARROW
   ;

POS
   : SUP PLUS
   ;

NEG
   : SUP MINUS
   ;

DOWNARROW
   : '\\downarrow'
   ;

ABS_VARIABLE
   : '|' VARIABLE '|'
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

DELTA_UC
   : '\\Delta'
   ;

ALPHA
   : '\\alpha'
   ;

BETA
   : '\\beta'
   ;

CAL
   : '\\cal'
   ;

CDOT
   : '\\cdot'
   ;

CFRAC
   : '\\cfrac'
   ;

CHI
   : '\\chi'
   ;

DELTA
   : '\\delta'
   ;

EPSILON
   : '\\epsilon'
   ;

ETA
   : '\\eta'
   ;

GAMMA
   : '\\gamma'
   ;

GAMMA_UC
   : '\\Gamma'
   ;

HAT
   : '\\hat'
   ;

HBAR
   : '\\hbar'
   ;

KAPPA
   : '\\kappa'
   ;

LAMBDA
   : '\\lambda'
   ;

NABLA
   : '\\nabla'
   ;

LAMBDA_UC
   : '\\Lambda'
   ;

LOG
   : '\\log'
   ;

MP
   : '\\mp'
   ;

MU
   : '\\mu'
   ;

NU
   : '\\nu'
   ;

OMEGA
   : '\\omega'
   ;

PHI
   : '\\phi'
   ;

PI
   : '\\pi'
   ;

PM
   : '\\pm'
   ;

PRIME
   : '\\prime'
   ;

PSI
   : '\\psi'
   ;

RHO
   : '\\rho'
   ;

SIGMA
   : '\\sigma'
   ;

SQRT
   : '\\sqrt'
   ;

TAU
   : '\\tau'
   ;

THETA
   : '\\theta'
   ;

TILDE
   : '\\tilde'
   ;

UPARROW
   : '\\uparrow'
   ;

VAREPSILON
   : '\\varepsilon'
   ;

VARPHI
   : '\\varphi'
   ;

VEC
   : '\\vec'
   ;

XI
   : '\\xi'
   ;

ZETA
   : '\\zeta'
   ;

