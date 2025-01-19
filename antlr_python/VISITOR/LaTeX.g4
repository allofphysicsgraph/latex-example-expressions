//Referenced antlr/grammars-v4/calculator.g4



grammar LaTeX;

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
   : 'x'
   ;

constant
   : 'PI'
   ;

relop
   : EQUALS
   ;

LB
   : '{'
   ;

RB
   : '}'
   ;

LP
   : '('
   ;

RP
   : ')'
   ;

LBR
   : '['
   ;

RBR
   : ']'
   ;

binop
   : PLUS
   | MINUS
   | MUL
   | DIVIDE
   ;

PLUS
   : '+'
   ;

MINUS
   : '-'
   ;

MUL
   : '*'
   ;

DIVIDE
   : '/'
   ;

EQUALS
   : '='
   ;

INTEGER
   : ZERO
   | DIGIT_NON_ZERO DIGIT*
   ;

fragment ZERO
   : '0'
   ;

fragment DIGIT_NON_ZERO
   : [1-9]
   ;

fragment DIGIT
   : ZERO
   | DIGIT_NON_ZERO
   ;

WS
   : [ \r\n\t] -> skip
   ;

