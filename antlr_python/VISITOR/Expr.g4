grammar Expr;

prog :  stat+
	;

stat:  	expr NEWLINE
	| equation NEWLINE
    | factorial NEWLINE
    | factorial factorial NEWLINE
    | NEWLINE
	;

expr: 
	<assoc=right> expr '^' expr # expo
	| expr op=('*' | '/'|'\\times'|'\\cdot'|'\\div') expr # mul_div
	| expr op=('+' | '-') expr # add_sub
	| op=('+'|'-') expr # pm_expr
	| INT # integer
	| VAR # var
	| INT VAR # integer_var
	| '(' expr ')' # parens 
	| '(' expr ')' '(' expr ')' # parens_parens
	| fraction # frac
    | '{' expr '}' # braces
    ;


factorial:
    expr '!'
    ;


fraction:
    '\\frac' numerator denominator
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
VAR : 'x'|'y'|'z'|'a'|'b'|'c'|'\\theta';

NEWLINE : '\n';

WS : [ \t]+ -> skip;
