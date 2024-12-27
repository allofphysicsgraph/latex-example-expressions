/*
 ANTLR4 LaTeX Math Grammar

 Ported from latex2sympy by @augustt198 https://github.com/augustt198/latex2sympy See license in
 LICENSE.txt
 */

/*
 After changing this file, it is necessary to run `python setup.py antlr` in the root directory of
 the repository. This will regenerate the code in `sympy/parsing/latex/_antlr/*.py`.
 */

grammar LaTeX;
import CommonLexerRules; 
options {
	language = Python3;
}

math: relation;

relation:
  relation EQUAL relation # relation_EQUAL_relation
  | relation LT relation # relation_LT_relation 
  | relation LTE relation # relation_LTE_relation 
  | relation GT relation # relation_GT_relation
  | relation GTE relation # relation_GTE_relation
  | relation NEQ relation # relation_NEQ_relation
	| expr # relation_expr;

equality: expr EQUAL expr;

expr: additive;

additive: additive ADD additive # additive_add_additive
    | additive SUB additive # additive_sub_additive
    | mp # additive_mp;

// mult part
mp:
	mp (MUL | CMD_TIMES | CMD_CDOT | DIV | CMD_DIV | COLON) mp
	| unary;

mp_nofunc:
	mp_nofunc (
		MUL
		| CMD_TIMES
		| CMD_CDOT
		| DIV
		| CMD_DIV
		| COLON
	) mp_nofunc
	| unary_nofunc;

unary: (ADD | SUB) unary | postfix+;

unary_nofunc:
	(ADD | SUB) unary_nofunc
	| postfix postfix_nofunc*;

postfix: exp postfix_op*;
postfix_nofunc: exp_nofunc postfix_op*;
postfix_op: BANG | eval_at;

eval_at:
	BAR (eval_at_sup | eval_at_sub | eval_at_sup eval_at_sub);

eval_at_sub: UNDERSCORE L_BRACE (expr | equality) R_BRACE;

eval_at_sup: CARET L_BRACE (expr | equality) R_BRACE;

exp: exp CARET (atom | L_BRACE expr R_BRACE) subexpr? | comp;

exp_nofunc:
	exp_nofunc CARET (atom | L_BRACE expr R_BRACE) subexpr?
	| comp_nofunc;

comp:
	group
	| abs_group
	| func
	| atom
	| floor
	| ceil;

comp_nofunc:
	group
	| abs_group
	| atom
	| floor
	| ceil;

group:
	L_PAREN expr R_PAREN
	| L_BRACKET expr R_BRACKET
	| L_BRACE expr R_BRACE
	| L_BRACE_LITERAL expr R_BRACE_LITERAL;

abs_group: BAR expr BAR;

number: DIGIT+ (',' DIGIT DIGIT DIGIT)* ('.' DIGIT+)?;

atom: (LETTER | SYMBOL) (subexpr? SINGLE_QUOTES? | SINGLE_QUOTES? subexpr?)
	| number
	| DIFFERENTIAL
	| mathit
	| frac
	| binom
	| bra
	| ket;

bra: L_ANGLE expr (R_BAR | BAR);
ket: (L_BAR | BAR) expr R_ANGLE;

mathit: CMD_MATHIT L_BRACE mathit_text R_BRACE;
mathit_text: LETTER*;

frac: CMD_FRAC (upperd = DIGIT | L_BRACE upper = expr R_BRACE)
    (lowerd = DIGIT | L_BRACE lower = expr R_BRACE);

binom:
	(CMD_BINOM | CMD_DBINOM | CMD_TBINOM) L_BRACE n = expr R_BRACE L_BRACE k = expr R_BRACE;

floor: L_FLOOR val = expr R_FLOOR;
ceil: L_CEIL val = expr R_CEIL;

func_normal:
	FUNC_EXP # EXP 
	| FUNC_LOG  # LOG
	| FUNC_LG   # LG
	| FUNC_LN   # LN
	| FUNC_SIN  # SIN
	| FUNC_COS  # COS
	| FUNC_TAN  # TAN
	| FUNC_CSC  # CSC
	| FUNC_SEC  # SEC
	| FUNC_COT  # COT
	| FUNC_ARCSIN   # ARCSIN
	| FUNC_ARCCOS   # ARCCOS
	| FUNC_ARCTAN   # ARCTAN
	| FUNC_ARCCSC   # ARCCSC
	| FUNC_ARCSEC   # ARCSEC
	| FUNC_ARCCOT   # ARCCOT
	| FUNC_SINH # SINH
	| FUNC_COSH # COSH
	| FUNC_TANH # TANH
	| FUNC_ARSINH   # ARSINH
	| FUNC_ARCOSH   # ARCOSH
	| FUNC_ARTANH  # ARTANH
    ;

func:
	func_normal (subexpr? supexpr? | supexpr? subexpr?) (
		L_PAREN func_arg R_PAREN
		| func_arg_noparens
	)
	| (LETTER | SYMBOL) (subexpr? SINGLE_QUOTES? | SINGLE_QUOTES? subexpr?) // e.g. f(x), f_1'(x)
	L_PAREN args R_PAREN
	| FUNC_INT (subexpr supexpr | supexpr subexpr)? (
		additive? DIFFERENTIAL
		| frac
		| additive
	)
	| FUNC_SQRT (L_BRACKET root = expr R_BRACKET)? L_BRACE base = expr R_BRACE
	| FUNC_OVERLINE L_BRACE base = expr R_BRACE
	| (FUNC_SUM | FUNC_PROD) (subeq supexpr | supexpr subeq) mp
	| FUNC_LIM limit_sub mp;

args: (expr ',' args) | expr;

limit_sub:
	UNDERSCORE L_BRACE (LETTER | SYMBOL) LIM_APPROACH_SYM expr (
		CARET ((L_BRACE (ADD | SUB) R_BRACE) | ADD | SUB)
	)? R_BRACE;

func_arg: expr | (expr ',' func_arg);
func_arg_noparens: mp_nofunc;

subexpr: UNDERSCORE (atom | L_BRACE expr R_BRACE);
supexpr: CARET (atom | L_BRACE expr R_BRACE);

subeq: UNDERSCORE L_BRACE equality R_BRACE;
supeq: CARET L_BRACE equality R_BRACE;
