grammar Expr;
options { tokenVocab=ModeTagsLexer;}

prog
   : stat+
   ;

stat
   : expr          # expression           
   | equation      # eqtn
   | '(' trig_function ')' '(' trig_function ')' # trig_parens_parens
   | trig_function trig_function+ # trig_function_multi
   | trig_function # trig_function_single
   | ceiling       # clng
   | floor         # flr
   | factorial     # fctrl
   | func_normal   # fnc_nrml
;

func_normal:
    lg
   | ln
   | log
   ;

trig_function: 
    cos
   | sin
   | tan
   ;

expr
   : < assoc = right > expr '^' expr # expo
   | expr op = ('*' | '/' | '\\times' | '\\cdot' | '\\div') expr # mul_div
   | expr op = ('+' | '-') expr # add_sub
   | expr op = ('>' | '<' | '\\neq' | '\\leq' | '\\geq' | '\\le' | '\\ge') expr # expr_relop_expr
   | '|' expr '|' # abs_expr
   | var '{' expr '}' # var_braces
   | '{' expr '}' var # braces_var
   | '{' expr '}' # braces
   | '(' expr ')' '(' expr ')' # parens_parens
   | '(' expr ')' var # parens_var
   | var '(' expr ')' # var_parens
   | '(' expr ')' # parens
   | '[' expr ']' var  # brackets_var
   | var '[' expr ']'  # brackets_var
   | '[' expr ']'  # brackets
   | fraction  # frac
   | INT var # integer_var
   | INT # integer
   | FLOAT var # Flt_var 
   | FLOAT # Flt
   | var var # var_var
   | var # variable
   | symbol # symbl
   | function # fnctn
   ;

// TODO Check
limit
    : '\\lim' '_' '{' var '\\to' e1=expr '}' e2 = expr
	| '\\lim' '_' '{' var '\\rightarrow' e1=expr '}' e2 = expr
	| '\\lim' '_' '{' var '\\Rightarrow' e1=expr '}' e2 = expr
	| '\\lim' '_' '{' var '\\longrightarrow' e1=expr '}' e2 = expr
	| '\\lim' '_' '{' var '\\Longrightarrow' e1=expr '}' e2 = expr
	| '\\lim' '_' '{' var '\\to' e1=expr  sup= (PLUS | MINUS)? '}' e2 = expr
	| '\\lim' '_' '{' var '\\rightarrow' e1=expr  sup= (PLUS | MINUS)? '}' e2 = expr
    ;
PLUS:
    '+'
    ;
MINUS:
    '-'
    ;
hbar
   : '\\hbar'
   ;

langle
   : '\\langle'
   ;

psi
   : '\\psi'
   ;

overline:
	'\\overline' '{' expr '}' ;

vec
   : '\\vec' '{' expr '}'
   ;

hat
   : '\\hat' '{' expr '}'
   ;


function
   : 'f' '(' var (',' var)* ')'
   ;

integral
   : '\\int' e = expr 'd' v = var
   ;

factorial
   : expr '!'        # factorial_single
   | factorial '!'   # factorial_recursive
   ;

log
   : '\\log' '_' '{' e1 = expr '}' e2 = expr
   | '\\log' '_' a1 = atom e2 = expr
   ;

lg
   : '\\lg' e = expr
   ;

exp
   : '\\exp' e = expr
   ;

ln
   : '\\ln' e = expr
   ;

floor
   : '\\lfloor' e = expr '\\rfloor'
   ;

ceiling
   : '\\lceil' e = expr '\\rceil'
   ;

sin
   : '\\sin' trig_function 
   | '\\sin' atom
   | '\\sin' '(' expr ')'
   ;

arccos
   : '\\arccos' atom
   | '\\arccos' '(' expr ')'
   ;

arccot
   : '\\arccot' atom
   | '\\arccot' '(' expr ')'
   ;

arccsc
   : '\\arccsc' atom
   | '\\arccsc' '(' expr ')'
   ;

arcosh
   : '\\arcosh' atom
   | '\\arcosh' '(' expr ')'
   ;

arcsec
   : '\\arcsec' atom
   | '\\arcsec' '(' expr ')'
   ;

arcsin
   : '\\arcsin' atom
   | '\\arcsin' '(' expr ')'
   ;

arctan
   : '\\arctan' atom
   | '\\arctan' '(' expr ')'
   ;

arsinh
   : '\\arsinh' atom
   | '\\arsinh' '(' expr ')'
   ;

artanh
   : '\\artanh' atom
   | '\\artanh' '(' expr ')'
   ;

cos
   : '\\cos' atom
   | '\\cos' '(' expr ')'
   ;

cosh
   : '\\cosh' atom
   | '\\cosh' '(' expr ')'
   ;

cot
   : '\\cot' atom
   | '\\cot' '(' expr ')'
   ;

csc
   : '\\csc' atom
   | '\\csc' '(' expr ')'
   ;

sec
   : '\\sec' atom
   | '\\sec' '(' expr ')'
   ;

sinh
   : '\\sinh' atom
   | '\\sinh' '(' expr ')'
   ;

tanh
   : '\\tanh' atom
   | '\\tanh' '(' expr ')'
   ;

tan
   : '\\tan' atom
   | '\\tan' '(' expr ')'
   ;

atom
   : var
   | INT
   | FLOAT
   ;

FLOAT
   : INT? ('.' [0-9]+)
   | '-' INT? ('.' [0-9]+)
 ;

sum
   : '\\sum' '_' '{' (e0 = expr | eq0 = equation) '}' '^' '{' e1 = expr '}' e2 = expr
   ;

product
   : '\\prod' '_' '{' (e0 = expr | eq0 = equation) '}' '^' '{' e1 = expr '}' e2 = expr
   ;


fraction
   : FRAC numerator denominator 
   ;

numerator:
    SINGLE_DIGIT
    ;
denominator:
    SINGLE_DIGIT_NON_ZERO
    ;

equation
   : lhs = expr equals = EQUALS rhs = expr
   ;

relational
   : expr relop expr
   ;

relop
   : '>'
   ;


EQUALS
   : '='
   ;

SINGLE_DIGIT_NON_ZERO:  [1-9];
SINGLE_DIGIT:  [0-9];
INT:
    '0' | SINGLE_DIGIT_NON_ZERO SINGLE_DIGIT* ; 


sqrt
    : '\\sqrt' '{' expr '}'
    ;


var
   : 'K' # var_K
   | 'G' # var_G
   | 'x' # var_x
   | 'y' # var_y
   | 'z' # var_z
   | 'a' # var_a
   | 'b' # var_b
   | 'c' # var_c
   | 'n' # var_n
   | 'h' # var_h
   | 'k' # var_k
   | 'u' # var_u
   | 'v' # var_v
   | 'w' # var_w
   | '\\theta' # var_theta
   | '\\alpha' # var_alpha
   | '\\beta' # var_beta
   | var PRIME # var_prime   
   ;


symbol
   : var '_' '{' var '}' # var_underscore_braces_var
   | var '_' INT # var_underscore_int
   | var '_' '{' INT '}' # var_underscore_braces_int
   | var '_' var # var_underscore_var
   | '\\pi' # pi 
   | '\\infty'  # infty
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
   : ('\\left\\'|'\\right\\'|'\\!'|'\\;'|'\\:'| '\\quad'| '\\qquad' |'\\thickspace'|'\\,' | '\\negthickspace'|'\\displaystyle' | '\\left' | '\\right' | '\\begin{align}' | '\\end{align}'|'\\negmedspace'|'\\medspace'|'\\negthinspace'|'\\thinspace') -> skip
   ;

NEWLINE
   : '\n' -> skip
   ;

WS
   : [ \t]+ -> skip
   ;

