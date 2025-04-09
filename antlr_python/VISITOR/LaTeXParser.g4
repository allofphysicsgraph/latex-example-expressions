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

sum
    : SUM sub_braces SUP VARIABLE
    | SUM sub_braces SUP INTEGER
    | SUM sub_braces SUP INFTY
    | SUM sub_braces sup_braces
    ;

sub_braces
    :  SUB LB simple_assignment RB
    ;
sup_braces
    : SUP LB simple_expression RB
    ;

simple_assignment
    : VARIABLE EQUALS INTEGER
    | VARIABLE EQUALS VARIABLE PLUS INTEGER
    | VARIABLE EQUALS MINUS INFTY
    ;

simple_expression
    : INTEGER VARIABLE
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

