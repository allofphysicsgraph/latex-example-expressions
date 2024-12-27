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
  | additive # relation_additive;

equality: additive EQUAL additive;


additive: additive ADD additive # additive_add_additive
    | additive SUB additive # additive_sub_additive
    | mp # additive_mp;

// mult part
mp:
	| mp MUL mp
    | mp CMD_TIMES mp 
    | mp CMD_CDOT mp 
    | mp DIV mp  
    | mp CMD_DIV mp  
    | mp COLON mp
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

unary: ADD unary | SUB unary | postfix+;

unary_nofunc:
	ADD unary_nofunc | SUB unary_nofunc
	| postfix postfix_nofunc*;

postfix: exp postfix_op*;
postfix_nofunc: exp_nofunc postfix_op*;
postfix_op: BANG | eval_at;

eval_at:
	BAR eval_at_sup 
    | BAR eval_at_sub |  BAR eval_at_sup eval_at_sub;

eval_at_sub: UNDERSCORE L_BRC (additive | equality) R_BRC;

eval_at_sup: CARET L_BRC (additive | equality) R_BRC;

exp: exp CARET (atom | L_BRC additive R_BRC) subexpr? | comp;

exp_nofunc:
	exp_nofunc CARET (atom | L_BRC additive R_BRC) subexpr?
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
	LP additive RP 
	| L_BRK additive R_BRK
	| L_BRC additive R_BRC
	| L_BRACE_LITERAL additive R_BRACE_LITERAL;

abs_group: BAR additive BAR;

//improve
number: INT+ (',' DIGIT DIGIT DIGIT)* ('.' DIGIT+)?;
INT: '0' | [1-9][0-9]* ; 

//review
//(LETTER | SYMBOL) (subexpr? SINGLE_QUOTES? | SINGLE_QUOTES? subexpr?)

atom: 
	  number
	| DIFFERENTIAL
	| mathit
	| frac
	| binom
	| bra
	| ket;

bra: L_ANGLE additive (R_BAR | BAR);
ket: (L_BAR | BAR) additive R_ANGLE;

mathit: CMD_MATHIT L_BRC mathit_text R_BRC;
mathit_text: LETTER*;

frac: CMD_FRAC (upperd = DIGIT | L_BRC upper = additive R_BRC)
    (lowerd = DIGIT | L_BRC lower = additive R_BRC);

binom:
	(CMD_BINOM | CMD_DBINOM | CMD_TBINOM) L_BRC n = additive R_BRC L_BRC k = additive R_BRC;

floor: L_FLOOR val = additive R_FLOOR;
ceil: L_CEIL val = additive R_CEIL;

func_normal:
	EXP # EXP 
	| LOG  # LOG
	| LG   # LG
	| LN   # LN
	| SIN  # SIN
	| COS  # COS
	| TAN  # TAN
	| CSC  # CSC
	| SEC  # SEC
	| COT  # COT
	| ARCSIN   # ARCSIN
	| ARCCOS   # ARCCOS
	| ARCTAN   # ARCTAN
	| ARCCSC   # ARCCSC
	| ARCSEC   # ARCSEC
	| ARCCOT   # ARCCOT
	| SINH # SINH
	| COSH # COSH
	| TANH # TANH
	| ARSINH   # ARSINH
	| ARCOSH   # ARCOSH
	| ARTANH  # ARTANH
    ;

func:
	func_normal (subexpr? supexpr? | supexpr? subexpr?) (
		LP func_arg RP 
		| func_arg_noparens
	)
	| (LETTER | SYMBOL) (subexpr? SINGLE_QUOTES? | SINGLE_QUOTES? subexpr?) // e.g. f(x), f_1'(x)
	LP args RP 
	| FUNC_INT (subexpr supexpr | supexpr subexpr)? (
		additive? DIFFERENTIAL
		| frac
		| additive
	)
	| FUNC_SQRT (L_BRK root = additive R_BRK)? L_BRC base = additive R_BRC
	| FUNC_OVERLINE L_BRC base = additive R_BRC
	| (FUNC_SUM | FUNC_PROD) (subeq supexpr | supexpr subeq) mp
	| LIM limit_sub mp;

args: (additive ',' args) | additive;

limit_sub:
	UNDERSCORE L_BRC (LETTER | SYMBOL) LIM_APPROACH_SYM additive (
		CARET ((L_BRC (ADD | SUB) R_BRC) | ADD | SUB)
	)? R_BRC;

func_arg: additive | (additive ',' func_arg);
func_arg_noparens: mp_nofunc;

subexpr: UNDERSCORE (atom | L_BRC additive R_BRC);
supexpr: CARET (atom | L_BRC additive R_BRC);

subeq: UNDERSCORE L_BRC equality R_BRC;
