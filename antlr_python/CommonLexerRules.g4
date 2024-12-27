grammar LaTeX;
WS: [ \t\r\n]+ -> skip;
THINSPACE: ('\\,' | '\\thinspace') -> skip;
MEDSPACE: ('\\:' | '\\medspace') -> skip;
THICKSPACE: ('\\;' | '\\thickspace') -> skip;
QUAD: '\\quad' -> skip;
QQUAD: '\\qquad' -> skip;
NEGTHINSPACE: ('\\!' | '\\negthinspace') -> skip;
NEGMEDSPACE: '\\negmedspace' -> skip;
NEGTHICKSPACE: '\\negthickspace' -> skip;
CMD_LEFT: '\\left' -> skip;
CMD_RIGHT: '\\right' -> skip;

IGNORE:
	(
		'\\vrule'
		| '\\vcenter'
		| '\\vbox'
		| '\\vskip'
		| '\\vspace'
		| '\\hfil'
		| '\\*'
		| '\\-'
		| '\\.'
		| '\\/'
		| '\\"'
		| '\\('
		| '\\='
	) -> skip;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

L_PAREN: '(';
R_PAREN: ')';
L_BRACE: '{';
R_BRACE: '}';
L_BRACE_LITERAL: '\\{';
R_BRACE_LITERAL: '\\}';
L_BRACKET: '[';
R_BRACKET: ']';

BAR: '|';

R_BAR: '\\right|';
L_BAR: '\\left|';

L_ANGLE: '\\langle';
R_ANGLE: '\\rangle';
FUNC_LIM: '\\lim';
LIM_APPROACH_SYM:
	'\\to'
	| '\\rightarrow'
	| '\\Rightarrow'
	| '\\longrightarrow'
	| '\\Longrightarrow';
FUNC_INT:
    '\\int'
    | '\\int\\limits';
FUNC_SUM: '\\sum';
FUNC_PROD: '\\prod';

FUNC_EXP: '\\exp';
FUNC_LOG: '\\log';
FUNC_LG: '\\lg';
FUNC_LN: '\\ln';
FUNC_SIN: '\\sin';
FUNC_COS: '\\cos';
FUNC_TAN: '\\tan';
FUNC_CSC: '\\csc';
FUNC_SEC: '\\sec';
FUNC_COT: '\\cot';

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

L_FLOOR: '\\lfloor';
R_FLOOR: '\\rfloor';
L_CEIL: '\\lceil';
R_CEIL: '\\rceil';

FUNC_SQRT: '\\sqrt';
FUNC_OVERLINE: '\\overline';

CMD_TIMES: '\\times';
CMD_CDOT: '\\cdot';
CMD_DIV: '\\div';
CMD_FRAC:
    '\\frac'
    | '\\dfrac'
    | '\\tfrac';
CMD_BINOM: '\\binom';
CMD_DBINOM: '\\dbinom';
CMD_TBINOM: '\\tbinom';

CMD_MATHIT: '\\mathit';

UNDERSCORE: '_';
CARET: '^';
COLON: ':';

fragment WS_CHAR: [ \t\r\n];
DIFFERENTIAL: 'd' WS_CHAR*? ([a-zA-Z] | '\\' [a-zA-Z]+);

LETTER: [a-zA-Z];
DIGIT: [0-9];

EQUAL: (('&' WS_CHAR*?)? '=') | ('=' (WS_CHAR*? '&')?);
NEQ: '\\neq';

LT: '<';
LTE: ('\\leq' | '\\le' | LTE_Q | LTE_S);
LTE_Q: '\\leqq';
LTE_S: '\\leqslant';

GT: '>';
GTE: ('\\geq' | '\\ge' | GTE_Q | GTE_S);
GTE_Q: '\\geqq';
GTE_S: '\\geqslant';

BANG: '!';

SINGLE_QUOTES: '\''+;

SYMBOL: '\\' [a-zA-Z]+;

