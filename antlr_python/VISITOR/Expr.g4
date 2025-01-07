grammar Expr;

prog: stat+ EOF;

stat:
    expr NEWLINE?                          # expressionStatement
    | equation NEWLINE?                     # equationStatement
    ;

expr:
    unaryExpr                               # unaryExpression
    ;

unaryExpr:
    factor ((op=('*' | '/' | '\\times' | '\\cdot' | '\\div')) factor)* # multiplicativeExpression
    ;

factor:
    term ((op=('+' | '-')) term)*         # additiveExpression
    ;

term:
    relationalExpr                          # relationalExpression
    ;

relationalExpr:
    atomicExpr (op=('<' | '>' | '=' | '\\neq' | '\\leq' | '\\geq' | '\\le' | '\\ge')) atomicExpr # binaryRelationalExpression
    | atomicExpr                            # atomicExpression
    ;

atomicExpr:
   '|' expr '|'                          # absExpression
    | var '{' expr '}'                      # varBraces
    | '{' expr '}' var                      # bracesVar
    | '{' expr '}'                          # bracesExpression
    | '(' expr ')' '(' expr ')'              # parensParens
    | '(' expr ')' var                      # parensVar
    | var '(' expr ')'                      # varParens
    | '(' expr ')'                          # parenthesizedExpression
    | '[' expr ']' var                      # bracketsVarPost
    | var '[' expr ']'                      # bracketsVarPre
    | '[' expr ']'                          # bracketedExpression
    | binomial                              # binomialExpression
    | fraction                              # fractionExpression
    | INT var                               # integerVariable
    | INT                                   # integerLiteral
    | FLOAT var                             # floatVariable
    | FLOAT                                 # floatLiteral
    | var var                               # variableVariable
    | var                                   # variable
    | symbol                                # symbolLiteral
    | functionCall                          # functionCallExpression
    | namedFunction                         # namedFunctionExpression
    ;

namedFunction:
    '\\arccos' argument  # arccos
    | '\\arccot' argument  # arccot
    | '\\arccsc' argument  # arccsc
    | '\\arcosh' argument  # arcosh
    | '\\arcsec' argument  # arcsec
    | '\\arcsin' argument  # arcsin
    | '\\arctan' argument  # arctan
    | '\\arsinh' argument  # arsinh
    | '\\artanh' argument  # artanh
    | '\\ceiling' argument # ceiling
    | '\\cos' argument      # cos
    | '\\cosh' argument     # cosh
    | '\\cot' argument      # cot
    | '\\csc' argument      # csc
    | '\\exp' argument      # exp
    | '\\floor' argument    # floor
    | '\\lg' argument       # lg
    | '\\ln' argument       # ln
    | '\\log' subSupArgument # logBase
    | '\\sec' argument      # sec
    | '\\sin' argument      # sin
    | '\\sinh' argument     # sinh
    | '\\sqrt' group        # sqrt
    | '\\tan' argument      # tan
    | '\\tanh' argument     # tanh
    ;

argument: atom | group;

subSupArgument: '_' group argument;

group: '{' expr '}';

functionCall:
    var '(' exprList? ')'
    ;

exprList:
    expr (',' expr)*
    ;

limit:
    '\\lim' '_' group ('\\to' | '\\rightarrow' | '\\Rightarrow' | '\\longrightarrow' | '\\Longrightarrow') (expr (PLUS | MINUS)?)? expr
    ;

sum:
    '\\sum' '_' (group | equation) '^' group expr
    ;

product:
    '\\prod' '_' (group | equation) '^' group expr
    ;

integral:
    '\\int' expr 'd' var
    ;

factorial:
    atomicExpr '!'
    ;

overline:
    '\\overline' group
    ;

vec:
    '\\vec' group
    ;

hat:
    '\\hat' group
    ;

binomial:
    '\\binom' numerator denominator
    | '\\tbinom' numerator denominator
    | '\\dbinom' numerator denominator
    ;

fraction:
    '\\frac' numerator denominator
    | '\\dfrac' numerator denominator
    | '\\tfrac' numerator denominator
    ;

numerator:
    INT            # numeratorInteger
    | group        # numeratorExpr
    ;

denominator:
    INT            # denominatorInteger
    | group        # denominatorExpr
    ;

equation:
    expr EQUALS expr
    ;

relop:
    '<' | '>' | '=' | '\\neq' | '\\leq' | '\\geq' | '\\le' | '\\ge'
    ;

symbol:
    var '_' groupVar         # varSubscriptVar
    | var '_' INT            # varSubscriptInt
    | '\\pi'                 # pi
    | '\\infty'              # infty
    | '\\gamma'               # gamma
    | '\\delta'               # delta
    | '\\epsilon'             # epsilon
    | '\\zeta'                # zeta
    | '\\eta'                 # eta
    | '\\iota'                # iota
    | '\\kappa'               # kappa
    | '\\lambda'              # lambda
    | '\\mu'                  # mu
    | '\\nu'                  # nu
    | '\\xi'                  # xi
    | '\\omicron'             # omicron
    | '\\rho'                 # rho
    | '\\sigma'               # sigma
    | '\\tau'                  # tau
    | '\\upsilon'             # upsilon
    | '\\phi'                 # phi
    | '\\chi'                 # chi
    | '\\psi'                 # psi
    | '\\omega'               # omega
    | '\\ell'                 # ell
    ;

groupVar: '{' var '}';

atom:
    var
    | INT
    | FLOAT
    ;

var:
    'K'   # varK
    | 'G'   # varG
    | 'x'   # varX
    | 'y'   # varY
    | 'z'   # varZ
    | 'a'   # varA
    | 'b'   # varB
    | 'c'   # varC
    | 'n'   # varN
    | 'h'   # varH
    | 'k'   # varSmallK
    | 'u'   # varU
    | 'v'   # varV
    | 'w'   # varW
    | '\\theta' # varTheta
    | '\\alpha' # varAlpha
    | '\\beta'  # varBeta
    ;


INT:  [0-9]+;
FLOAT: '-'? INT? '.' [0-9]+;

PLUS: '+';
MINUS: '-';
EQUALS: '=';
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;
IGNORE: ('\\left\\'|'\\right\\'|'\\!'|'\\;'|'\\:'| '\\quad'| '\\qquad' |'\\thickspace'|'\\,' | '\\negthickspace'|'\\displaystyle' | '\\left' | '\\right' | '\\begin{align}' | '\\end{align}'|'\\negmedspace'|'\\medspace'|'\\negthinspace'|'\\thinspace') -> skip;
