grammar Expr;

prog :  stat+
	;

stat:  	expr NEWLINE
	| equation NEWLINE
	| NEWLINE
	;

expr: 
	expr op=('*' | '/') expr # mul_div
	| expr op=('+' | '-') expr # add_sub
	| op=('+'|'-') expr # pm_expr
	| INT # integer
	| VAR # var
	| '(' expr ')' # parens 
	
	;

equation: lhs=expr equals=EQUALS rhs=expr;


EQUALS : '=' ; 
INT : 	'0' | [1-9][0-9]*;
VAR : 'x';

NEWLINE : '\n';

WS : [ \t]+ -> skip;
