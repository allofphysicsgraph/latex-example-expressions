//Referenced antlr/grammars-v4/calculator.g4

lexer grammar LaTeXLexer;

VARIABLE
   : 'a'
   | 'A'
   | 'b'
   | 'B'
   | 'c'
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
   | '\\over'
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

SUB
   : '_'
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





BAR: '|';
L_VERT: '\\lvert';
R_VERT: '\\rvert';
VERT: '\\vert';

NORM: '\\|';

L_FLOOR: '\\lfloor';
R_FLOOR: '\\rfloor';
LL_CORNER: '\\llcorner';
LR_CORNER: '\\lrcorner';

L_CEIL: '\\lceil';
R_CEIL: '\\rceil';
UL_CORNER: '\\ulcorner';
UR_CORNER: '\\urcorner';

L_LEFT: '\\left';
R_RIGHT: '\\right';
ML_LEFT: '\\mleft';
MR_RIGHT: '\\mright';

//functions
FUNC_LIM:  '\\lim';
LIM_APPROACH: '\\to' | '\\rightarrow' | '\\Rightarrow' | '\\longrightarrow' | '\\Longrightarrow';
FUNC_INT:  '\\int';
FUNC_SUM:  '\\sum';
FUNC_PROD: '\\prod';

FUNC_LOG:  '\\log';
FUNC_LN:   '\\ln';
FUNC_EXP: '\\exp';
FUNC_SIN:  '\\sin';
FUNC_COS:  '\\cos';
FUNC_TAN:  '\\tan';
FUNC_CSC:  '\\csc';
FUNC_SEC:  '\\sec';
FUNC_COT:  '\\cot';

FUNC_ARCSIN: '\\arcsin';
FUNC_ARCCOS: '\\arccos';
FUNC_ARCTAN: '\\arctan';
FUNC_ARCCSC: '\\arccsc';
FUNC_ARCSEC: '\\arcsec';
FUNC_ARCCOT: '\\arccot';

FUNC_SINH: '\\sinh';
FUNC_COSH: '\\cosh';
FUNC_TANH: '\\tanh';
FUNC_ARSINH: '\\arsinh';
FUNC_ARCOSH: '\\arcosh';
FUNC_ARTANH: '\\artanh';
FUNC_ARCSINH: '\\arcsinh';
FUNC_ARCCOSH: '\\arccosh';
FUNC_ARCTANH: '\\arctanh';

FUNC_SQRT: '\\sqrt';
FUNC_GCD: '\\gcd';
FUNC_LCM: '\\lcm';
FUNC_FLOOR: '\\floor';
FUNC_CEIL: '\\ceil';
FUNC_MAX: '\\max';
FUNC_MIN: '\\min';

FUNC_DET: '\\det';


//commands
CMD_TIMES: '\\times';
CMD_CDOT:  '\\cdot';
CMD_DIV:   '\\div';
CMD_FRAC:  '\\frac';
CMD_BINOM: '\\binom' | '\\tbinom' | '\\dbinom';
CMD_CHOOSE: '\\choose';
CMD_MOD: '\\mod';

CMD_MATHIT: '\\mathit';

CMD_OPERATORNAME: '\\operatorname';

COLON: ':';
SEMICOLON: ';';
PERIOD: '.';

fragment WS_CHAR: [ \t\r\n];
DIFFERENTIAL: 'd' WS_CHAR*? ([a-zA-Z] | '\\' [a-zA-Z]+);

EXP_E: 'e' | '\\exponentialE';
E_NOTATION_E: 'E';
LETTER_NO_E: [a-df-zA-DF-Z]; // exclude e for exponential function and e notation
fragment LETTER: [a-zA-Z];

MATRIX_XRIGHTARROW: '\\xrightarrow' | '\\xRightarrow';
TRANSFORM_EXCHANGE: '<->' | '<=>' | '\\leftrightarrow' | '\\Leftrightarrow';

NUMBER:
    DIGIT+ (COMMA DIGIT DIGIT DIGIT)*
    | DIGIT* (COMMA DIGIT DIGIT DIGIT)* PERIOD DIGIT+;

E_NOTATION: NUMBER E_NOTATION_E (SUB | PLUS)? DIGIT+;

IN: '\\in';
EQUAL: '==' | '\\equiv';
LTE: '\\leq' | '\\le' | '\\leqslant';
GT: '>';
GTE: '\\geq' | '\\ge' | '\\geqslant';
UNEQUAL: '!=' | '!==' | '\\ne' | '\\neq' | '\\not\\equiv';

BANG: '!';

fragment PERCENT_SIGN: '\\%';
PERCENT_NUMBER: NUMBER PERCENT_SIGN;

//Excludes some letters for use as e.g. constants in SYMBOL
fragment GREEK_LETTER:
    '\\char"000391' | //Alpha
    '\\alpha' |
    '\\char"000392' | //Beta
    '\\beta' |
    '\\Gamma' |
    '\\gamma' |
    '\\Delta' |
    '\\delta' |
    '\\char"000190' | //Epsilon
    '\\epsilon' |
    '\\varepsilon' |
    '\\char"000396' | //Zeta
    '\\zeta' |
    '\\char"000397' | //Eta
    '\\eta' |
    '\\Theta' |
    '\\theta' |
    '\\vartheta' |
    '\\char"000399' | //Iota
    '\\iota' |
    '\\char"00039A' | //Kappa
    '\\kappa' |
    '\\Lambda' |
    '\\lambda' |
    '\\char"00039C' | //Mu
    '\\mu' |
    '\\char"00039D' | //Nu
    '\\nu' |
    '\\Xi' |
    '\\xi' |
    '\\char"00039F' | //Omicron
    '\\omicron' |
    '\\Pi' |
    '\\varpi' |
    '\\char"0003A1' | //Rho
    '\\rho' |
    '\\varrho' |
    '\\Sigma' |
    '\\sigma' |
    '\\varsigma' |
    '\\char"0003A4' | //Tau
    '\\tau' |
    '\\Upsilon' |
    '\\upsilon' |
    '\\Phi' |
    '\\phi' |
    '\\varphi' |
    '\\char"0003A7' | //Chi
    '\\chi' |
    '\\Psi' |
    '\\psi' |
    '\\Omega' |
    '\\omega';

GREEK_CMD: GREEK_LETTER [ ]?;

fragment OTHER_SYMBOL:
    '\\Bbbk'  |
    '\\wp'  |
    '\\nabla'  |
    '\\bigstar'  |
    '\\angle'  |
    '\\nexists'  |
    '\\diagdown'  |
    '\\measuredangle'  |
    '\\eth'  |
    '\\emptyset'  |
    '\\diagup'  |
    '\\sphericalangle'  |
    '\\clubsuit'  |
    '\\varnothing'  |
    '\\Diamond'  |
    '\\complement'  |
    '\\diamondsuit'  |
    '\\imath'  |
    '\\Finv'  |
    '\\triangledown'  |
    '\\heartsuit'  |
    '\\jmath'  |
    '\\Game'  |
    '\\triangle'  |
    '\\spadesuit'  |
    '\\ell'  |
    '\\hbar'  |
    '\\vartriangle'  |
    '\\hslash'  |
    '\\blacklozenge'  |
    '\\lozenge'  |
    '\\blacksquare'  |
    '\\mho'  |
    '\\blacktriangle'  |
    '\\sharp'  |
    '\\prime'  |
    '\\Im'  |
    '\\flat'  |
    '\\square'  |
    '\\backprime'  |
    '\\Re'  |
    '\\natural'  |
    '\\surd'  |
    '\\circledS';
OTHER_SYMBOL_CMD: OTHER_SYMBOL [ ]?;

fragment PARTIAL_CMD: '\\partial';
fragment EMPTYSET: '\\emptyset';
SYMBOL: PI | PARTIAL_CMD | INFTY | EMPTYSET;


