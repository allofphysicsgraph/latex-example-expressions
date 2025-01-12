parser grammar ExprParser;


options { tokenVocab = ExprLexer; }
prog
   : stat+
   ;

stat
   : expr # expression
   | LP trig_function RP LP trig_function RP # trig_parens_parens
   | trig_function trig_function+ # trig_function_multi
   | trig_function # trig_function_single
   | floor # flr
   | func_normal # fnc_nrml
   ;

func_normal
   : lg
   | ln
   | log
   ;

trig_function
   : cos
   | sin
   ;

expr
   : < assoc = right > expr SUP expr # expo
   | expr op = (MUL | DIV | TIMES | CDOT) expr # mul_div
   | expr op = (ADD | SUB) expr # add_sub
   | expr op = (GT | LT | UNEQUAL | LTE | GTE) expr # expr_relop_expr
   | var LB expr RB # var_braces
   | LB expr RB var # braces_var
   | LB expr RB # braces
   | LP expr RP LP expr RP # parens_parens
   | LP expr RP var # parens_var
   | var LP expr RP # var_parens
   | LP expr RP # parens
   | LBR expr RBR var # brackets_var
   | var LBR expr RBR # brackets_var
   | LBR expr RBR # brackets
   | fraction # frac
   | INT var # integer_var
   | INT # integer
   | FLOAT var # Flt_var
   | FLOAT # Flt
   | var var # var_var
   | var # variable
   | symbol # symbl
   ;

sin
   : SIN trig_function
   | SIN atom
   | SIN LP expr RP
   ;

hbar
   : HBAR
   ;

hat
   : HAT LB expr RB
   ;

log
   : LOG
   ;

lg
   : LG
   ;

exp
   : EXP
   ;

ln
   : LN
   ;

floor
   : LFLOOR
   ;

cos
   : COS atom
   | COS LP expr RP
   ;

fraction
   : FRAC numerator denominator
   ;

numerator
   : SINGLE_DIGIT
   ;

denominator
   : SINGLE_DIGIT_NON_ZERO
   ;

var
   : K_U_VAR # var_K
   | G_U_VAR # var_G
   | X_VAR # var_x
   | Y_VAR # var_y
   | Z_VAR # var_z
   | A_VAR # var_a
   | B_VAR # var_b
   | C_VAR # var_v
   | N_VAR # var_n
   | H_VAR # var_h
   | K_VAR # var_k
   | U_VAR # var_u
   | V_VAR # var_v
   | W_VAR # var_w
   | THETA # var_theta
   | ALPHA # var_alpha
   | BETA # var_beta
   | var PRIME # var_prime
   ;

symbol
   : var SUB LB var RB # var_underscore_braces_var
   | var SUB INT # var_underscore_int
   | var SUB LB INT RB # var_underscore_braces_int
   | var SUB var # var_underscore_var
   ;

atom
   : var
   | INT
   | FLOAT
   ;

