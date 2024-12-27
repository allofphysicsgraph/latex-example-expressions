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

math: expression;


expression:
    SUB expression                                              # Unary // Unary minus sign (negative numbers)
    | ADD expression                                            # UnaryPlus // Unary plus sign (positive numbers)
    | expression op = ('^' | '**') expression                   # Pow // expr_1 to the expr_2 th power
    | expression op = (MUL | DIV|CMD_TIMES|CMD_DIV|COLON) expression                    # MulDiv // Multiplication or division
    | '(' expression ')'                                        # Parenthesis // Expression within parentheses
    | '[' expression ']'                                        # Parenthesis // Expression within parentheses
    | '{' expression '}'                                        # Parenthesis // Expression within parentheses
    | expression '(' expression ')'                             # Mult // Multiplication without sign
    | '(' expression ')' expression                             # Mult // Multiplication without sign
    | expression op = (ADD | SUB) expression                    # AddSub // Addition or subtraction
    | relation  # Rltn
    | number                                                    # Nm // Single integer or float number
    ;

relation:
  relation EQUAL relation # relation_EQUAL_relation
  | relation LT relation # relation_LT_relation 
  | relation LTE relation # relation_LTE_relation 
  | relation GT relation # relation_GT_relation
  | relation GTE relation # relation_GTE_relation
  | relation NEQ relation # relation_NEQ_relation
  | atom # relation_atom
  ;

//improve
number: INT+ (',' DIGIT DIGIT DIGIT)* ('.' DIGIT+)?;
INT: '0' | [1-9][0-9]* ; 

atom: 
	  number
    ;

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

