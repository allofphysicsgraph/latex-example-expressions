//Referenced antlr/grammars-v4/calculator.g4

parser grammar LaTeXParser;


options { tokenVocab = LaTeXLexer; }
prog
   : equation+
   | expression
   ;

equation
   : expression relop expression
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
   | POW
   ;

