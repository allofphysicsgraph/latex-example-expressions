grammar Expr;

prog :  stat+
	;

stat:  expr NEWLINE
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

INT : 	'0' | [1-9][0-9]*;
VAR : 'x';

NEWLINE : '\n';

WS : [ \t]+ -> skip;
