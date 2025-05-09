//Referenced antlr/grammars-v4/calculator.g4

parser grammar LaTeXParser;


options { tokenVocab = LaTeXLexer; }
prog
   : equation+
   ;

equation
   : BEGIN_EQUATION symbol EQUALS sum symbol symbol END_EQUATION
   | BEGIN_EQUATION VARIABLE EQUALS VARIABLE END_EQUATION
   | BEGIN_EQUATION expression EQUALS expression  END_EQUATION
   ;


symbol:
    VARIABLE SUB VARIABLE
    ;

exp:
    FUNC_EXP
    ;

frac
    : CMD_FRAC LB expression RB LB expression RB
    ;
lim
   : LIM VARIABLE RB
   | LIM VARIABLE LIM_APPROACH INFTY RB
   | LIM VARIABLE LIM_APPROACH POS_INFTY RB
   | LIM VARIABLE LIM_APPROACH NEG_INFTY RB
   | LIM VARIABLE LIM_APPROACH INTEGER RB
   | LIM VARIABLE LIM_APPROACH INTEGER POS RB
   | LIM VARIABLE LIM_APPROACH INTEGER NEG RB
   | LIM VARIABLE DOWNARROW INTEGER RB
   | LIM ABS_VARIABLE LIM_APPROACH INFTY RB
   ;

sum
   : FUNC_SUM SUB LB LANGLE VARIABLE VARIABLE RANGLE RB
   | FUNC_SUM SUB LB VARIABLE COMMA VARIABLE RB
   | FUNC_SUM SUB LB VARIABLE EQUALS INTEGER RB SUP INFTY
   | FUNC_SUM SUB LB VARIABLE EQUALS INTEGER RB SUP INTEGER
   | FUNC_SUM SUB LB VARIABLE EQUALS INTEGER RB SUP LB INFTY RB
   | FUNC_SUM SUB LB VARIABLE EQUALS INTEGER RB SUP LB VARIABLE MINUS INTEGER RB
   | FUNC_SUM SUB LB VARIABLE EQUALS INTEGER RB SUP LB VARIABLE SUB VARIABLE RB
   | FUNC_SUM SUB LB VARIABLE EQUALS INTEGER RB SUP LB VARIABLE RB
   | FUNC_SUM SUB LB VARIABLE EQUALS INTEGER RB SUP VARIABLE
   | FUNC_SUM SUB LB VARIABLE EQUALS MINUS INFTY RB SUP INFTY
   | FUNC_SUM SUB LB VARIABLE EQUALS MINUS INFTY RB SUP LB INFTY RB
   | FUNC_SUM SUB LB VARIABLE EQUALS NEG_INFTY RB SUP INFTY
   | FUNC_SUM SUB LB VARIABLE EQUALS NEG_INFTY RB SUP LB INFTY RB
   | FUNC_SUM SUB LB VARIABLE LT VARIABLE RB
   | FUNC_SUM SUB LB VARIABLE UNEQUAL VARIABLE RB
   | FUNC_SUM SUB LB VARIABLE RB
   | FUNC_SUM SUB LB VARIABLE VARIABLE RB
   | FUNC_SUM SUB VARIABLE
   ;

sub_braces
   : simple_assignment RB
   ;

sup_braces
   : SUP LB simple_expression RB
   ;

simple_assignment
   : VARIABLE EQUALS INTEGER
   | VARIABLE EQUALS VARIABLE PLUS INTEGER
   | VARIABLE EQUALS INFTY
   | VARIABLE EQUALS POS_INFTY
   | VARIABLE EQUALS NEG_INFTY
   ;

simple_expression
   : INTEGER VARIABLE
   | VARIABLE MINUS INTEGER
   | INFTY
   ;

expression
   : signedAtom (binop signedAtom)*
   | numeric_atom atom
   | atom numeric_atom
   | frac
   | expression (binop expression)+
   | atom SUB braces_expression
   | atom SUB braces_expression SUP braces_expression
   | atom SUP braces_expression
   ;

signedAtom
   : PLUS signedAtom
   | MINUS signedAtom
   | numeric_atom
   | atom
   ;

atom
   : variable
   ;

numeric_atom
   : number
   ;

number
   : INTEGER
   | FLOAT
   | constant
   ;

braces_expression 
    : LB expression RB
    ;
enclosed_expression
   :
   | LP expression RP
   | LBR expression RBR
   ;

variable
   : VARIABLE
   | VARIABLE SUB INTEGER
   ;

constant
   : PI
   ;

relop
   : EQUALS
   ;

binop
   : PLUS
   | MINUS
   | MUL
   | DIVIDE
   | SUP
   ;

