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
   ;

signedAtom
   : PLUS signedAtom
   | MINUS signedAtom
   | atom
   ;

atom
   : INTEGER
   | variable
   | constant
   | enclosed_expression
   ;

enclosed_expression
   :
   | LB expression RB
   | LP expression RP
   | LBR expression RBR
   ;

variable
   : X
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

