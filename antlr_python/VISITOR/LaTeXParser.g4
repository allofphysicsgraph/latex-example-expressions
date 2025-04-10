//Referenced antlr/grammars-v4/calculator.g4

parser grammar LaTeXParser;


options { tokenVocab = LaTeXLexer; }
prog
   : sum+
   | expression
   ;

equation
   : BEGIN_EQUATION sum END_EQUATION
   ;

lim
   : LIM VARIABLE RB
   | LIM VARIABLE TO INFTY RB
   | LIM VARIABLE TO POS_INFTY RB
   | LIM VARIABLE TO NEG_INFTY RB
   | LIM VARIABLE TO INTEGER RB
   | LIM VARIABLE TO INTEGER POS RB
   | LIM VARIABLE TO INTEGER NEG RB
   | LIM VARIABLE DOWNARROW INTEGER RB
   | LIM ABS_VARIABLE TO INFTY RB
   ;

sum
   : SUM SUB LB LANGLE VARIABLE VARIABLE RANGLE RB
   | SUM SUB LB VARIABLE COMMA VARIABLE RB
   | SUM SUB LB VARIABLE EQUALS INTEGER RB SUP INFTY
   | SUM SUB LB VARIABLE EQUALS INTEGER RB SUP INTEGER
   | SUM SUB LB VARIABLE EQUALS INTEGER RB SUP LB INFTY RB
   | SUM SUB LB VARIABLE EQUALS INTEGER RB SUP LB VARIABLE MINUS INTEGER RB
   | SUM SUB LB VARIABLE EQUALS INTEGER RB SUP LB VARIABLE RB
   | SUM SUB LB VARIABLE EQUALS INTEGER RB SUP VARIABLE
   | SUM SUB LB VARIABLE EQUALS MINUS INFTY RB SUP INFTY
   | SUM SUB LB VARIABLE EQUALS MINUS INFTY RB SUP LB INFTY RB
   | SUM SUB LB VARIABLE EQUALS NEG_INFTY RB SUP INFTY
   | SUM SUB LB VARIABLE EQUALS NEG_INFTY RB SUP LB INFTY RB
   | SUM SUB LB VARIABLE LT VARIABLE RB
   | SUM SUB LB VARIABLE NEQ VARIABLE RB
   | SUM SUB LB VARIABLE RB
   | SUM SUB LB VARIABLE VARIABLE RB
   | SUM SUB VARIABLE
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
   ;

signedAtom
   : PLUS signedAtom
   | MINUS signedAtom
   | numeric_atom
   | atom
   ;

atom
   : variable
   | enclosed_expression
   ;

numeric_atom
   : number
   ;

number
   : INTEGER
   | FLOAT
   | constant
   ;

enclosed_expression
   :
   | LB expression RB
   | LP expression RP
   | LBR expression RBR
   ;

variable
   : VARIABLE
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
   ;

