grammar Expr;

prog :  stat+
	;

stat:  	expr NEWLINE
	| equation NEWLINE
    | factorial NEWLINE
    | factorial factorial NEWLINE
    | integral NEWLINE
    | log NEWLINE
    | lg NEWLINE
    | ln NEWLINE
    | exp NEWLINE
    | sum NEWLINE
    | sin NEWLINE
    | floor NEWLINE
    | ceiling NEWLINE
    | NEWLINE
	;

expr: 
	<assoc=right> expr '^' expr # expo
	| expr op=('*' | '/'|'\\times'|'\\cdot'|'\\div') expr # mul_div
	| expr op=('+' | '-') expr # add_sub
	| op=('+'|'-') expr # pm_expr
	| '|' expr '|' # abs_expr
    | '{' expr '}' # braces
	| '(' expr ')' '(' expr ')' # parens_parens
	| '(' expr ')' # parens 
    | '(' expr ')' VAR # parens_var
    | binomial # binom
    | fraction # frac
	| INT # integer
    | INT VAR # integer_var
    | VAR '(' expr ')' # var_parens 
	| VAR # var
    | VAR VAR # var_var
    | symbol # symbl
    ;

integral:
    '\\int' e=expr 'd' v=VAR;

factorial:
    expr '!'
    ;

log:
    '\\log' '_' '{' e1=expr '}' e2=expr
    | '\\log' '_' a1=atom e2=expr
    ;
lg:
    '\\lg' e=expr ;

exp:
    '\\exp' e=expr;

ln:
    '\\ln' e=expr;

floor:
    '\\lfloor' e=expr '\\rfloor';

ceiling:
    '\\lceil' e=expr '\\rceil';

sin:
    '\\sin' atom 
    | '\\sin' '(' expr ')' 
    ;

atom:
    VAR
    | INT
    | FLOAT
    ;

FLOAT:
    INT ('.' [0-9]+)
    ;

sum:
    '\\sum' '_' '{' (e0=expr|eq0=equation) '}' '^' '{' e1=expr '}' e2=expr;

binomial:
    '\\binom' numerator denominator
    |'\\tbinom' numerator denominator
    |'\\dbinom' numerator denominator
    ;

fraction:
    '\\frac' numerator denominator
    |'\\dfrac' numerator denominator
    |'\\tfrac' numerator denominator
    ;

numerator:
    INT # numerator_integer
    |  '{' expr '}' # numerator_expr
    ;
denominator:
    INT # denominator_integer
    |  '{' expr '}' # denominator_expr
    ;

equation: lhs=expr equals=EQUALS rhs=expr
	| BEGIN_EQ NEWLINE? equation NEWLINE? END_EQ
	;

relational:
    expr relop expr
    ;

relop:
    '>'
    ;    

BEGIN_EQ: '\\begin{equation}' -> skip;
END_EQ: '\\end{equation}' -> skip;

EQUALS : '=' ; 
INT : 	'0' | [1-9][0-9]*;
VAR : 'x'|'y'|'z'|'a'|'b'|'c'|'h'|'k'|'\\theta';

symbol:
    VAR '_' '{' VAR '}'
    | VAR '_' INT
    | VAR '_' '{' INT '}'
    | VAR '_' VAR
    ;

NEWLINE : '\n';

WS : [ \t]+ -> skip;
