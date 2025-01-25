lexer grammar LaTeXLexer;

SQRT
   : '\\sqrt'
   ;

FRAC
   : '\\frac'
   ;

SUM
   : '\\sum'
   ;

PROD
   : '\\prod'
   ;

LIM
   : '\\lim'
   ;

INF
   : '\\inf'
   ;

SUP
   : '\\sup'
   ;

INJLIM
   : '\\injlim'
   ;

PROJLIM
   : '\\projlim'
   ;

VARLIMSUP
   : '\\varlimsup'
   ;

VARLIMINF
   : '\\varliminf'
   ;

VARINJLIM
   : '\\varinjlim'
   ;

VARPROJLIM
   : '\\varprojlim'
   ;

ARCCOS
   : '\\arccos'
   ;

ARCSIN
   : '\\arcsin'
   ;

ARCTAN
   : '\\arctan'
   ;

ARG
   : '\\arg'
   ;

COS
   : '\\cos'
   ;

COSH
   : '\\cosh'
   ;

COT
   : '\\cot'
   ;

COTH
   : '\\coth'
   ;

CSC
   : '\\csc'
   ;

DEG
   : '\\deg'
   ;

DET
   : '\\det'
   ;

EXP
   : '\\exp'
   ;

GCD
   : '\\gcd'
   ;

HOM
   : '\\hom'
   ;

KER
   : '\\ker'
   ;

LG
   : '\\lg'
   ;

LN
   : '\\ln'
   ;

LOG
   : '\\log'
   ;

MAX
   : '\\max'
   ;

MIN
   : '\\min'
   ;

PR
   : '\\Pr'
   ;

SEC
   : '\\sec'
   ;

SIN
   : '\\sin'
   ;

SINH
   : '\\sinh'
   ;

TAN
   : '\\tan'
   ;

TANH
   : '\\tanh'
   ;

DOTS_C
   : '\\dotsc'
   ;

DOTS_B
   : '\\dotsb'
   ;

DOTS_M
   : '\\dotsm'
   ;

DOTS_I
   : '\\dotsi'
   ;

DOTS_O
   : '\\dotso'
   ;

CDOTS
   : '\\cdots'
   ;

VDOTS
   : '\\vdots'
   ;

DDOTS
   : '\\ddots'
   ;

LDOTS
   : '\\ldots'
   ;

SQRT_SIGN
   : '\\sqrtsign'
   ;

OVERLINE
   : '\\overline'
   ;

OVERSET
   : '\\overset'
   ;

UNDERSET
   : '\\underset'
   ;

XLEFTARROW
   : '\\xleftarrow'
   ;

XRIGHTARROW
   : '\\xrightarrow'
   ;

VEC
   : '\\Vec'
   ;

VECT
   : '\\vect'
   ;

PMB
   : '\\pmb'
   ;

MATHBF
   : '\\mathbf'
   ;

MATHCAL
   : '\\mathcal'
   ;

MATHRM
   : '\\mathrm'
   ;

MATHSF
   : '\\mathsf'
   ;

MATHTT
   : '\\mathtt'
   ;

MATHIT
   : '\\mathit'
   ;

HAT
   : '\\hat'
   ;

HATHAT
   : '\\Hat{\\Hat{H}}'
   ;

CHECK
   : '\\Check'
   ;

CHECKCHECK
   : '\\Check{\\Check{C}}'
   ;

TILDE
   : '\\Tilde'
   ;

TILDETILDE
   : '\\Tilde{\\Tilde{T}}'
   ;

ACUTE
   : '\\Acute'
   ;

ACUTEACUTE
   : '\\Acute{\\Acute{A}}'
   ;

GRAVE
   : '\\Grave'
   ;

GRAVEGRAVE
   : '\\Grave{\\Grave{G}}'
   ;

DOT_ACCENT
   : '\\Dot'
   ;

DOTDOT_ACCENT
   : '\\Ddot'
   ;

BREVE
   : '\\Breve'
   ;

BREVEBREVE
   : '\\Breve{\\Breve{B}}'
   ;

BAR
   : '\\Bar'
   ;

BARBAR
   : '\\Bar{\\Bar{B}}'
   ;

VECVEC
   : '\\Vec{\\Vec{V}}'
   ;

DDDOT
   : '\\dddot'
   ;

DDDDOT
   : '\\ddddot'
   ;

LEFTROOT
   : '\\leftroot'
   ;

UPROOT
   : '\\uproot'
   ;

OVERBRACE
   : '\\overbrace'
   ;

UNDERBRACE
   : '\\underbrace'
   ;

UNDERLEFTARROW
   : '\\underleftarrow'
   ;

UNDERrightarrow
   : '\\underrightarrow'
   ;

UNDERleftrightarrow
   : '\\underleftrightarrow'
   ;

OVERLEFTARROW
   : '\\overleftarrow'
   ;

OVERrightarrow
   : '\\overrightarrow'
   ;

OVERleftrightarrow
   : '\\overleftrightarrow'
   ;

WIDEHAT
   : '\\widehat'
   ;

WIDETILDE
   : '\\widetilde'
   ;

RELBAR
   : '\\Relbar'
   ;

EQREF
   : '\\eqref'
   ;

REF
   : '\\ref'
   ;

PMOD
   : '\\pmod'
   ;

MOD_CMD
   : '\\mod'
   ;

POD
   : '\\pod'
   ;

TEXT
   : '\\text'
   ;

MBOX
   : '\\mbox'
   ;

HBOX
   : '\\hbox'
   ;

FBOX
   : '\\fbox'
   ;

CASES_ENV
   : '\\begin{cases}'
   ;

END_CASES_ENV
   : '\\end{cases}'
   ;

SMALLMATRIX_ENV
   : '\\begin{smallmatrix}'
   ;

END_SMALLMATRIX_ENV
   : '\\end{smallmatrix}'
   ;

MATRIX_ENV
   : '\\begin{matrix}'
   ;

END_MATRIX_ENV
   : '\\end{matrix}'
   ;

PMATRIX_ENV
   : '\\begin{pmatrix}'
   ;

END_PMATRIX_ENV
   : '\\end{pmatrix}'
   ;

BMATRIX_ENV
   : '\\begin{bmatrix}'
   ;

END_BMATRIX_ENV
   : '\\end{bmatrix}'
   ;

BMATRIX_ENV_BIG
   : '\\begin{Bmatrix}'
   ;

END_BMATRIX_ENV_BIG
   : '\\end{Bmatrix}'
   ;

VMATRIX_ENV
   : '\\begin{vmatrix}'
   ;

END_VMATRIX_ENV
   : '\\end{vmatrix}'
   ;

VMATRIX_ENV_BIG
   : '\\begin{Vmatrix}'
   ;

END_VMATRIX_ENV_BIG
   : '\\end{Vmatrix}'
   ;

SPLIT_ENV
   : '\\begin{split}'
   ;

END_SPLIT_ENV
   : '\\end{split}'
   ;

MULTLINE_ENV
   : '\\begin{multline}'
   ;

END_MULTLINE_ENV
   : '\\end{multline}'
   ;

GATHER_ENV
   : '\\begin{gather}'
   ;

END_GATHER_ENV
   : '\\end{gather}'
   ;

ALIGN_ENV
   : '\\begin{align}'
   ;

END_ALIGN_ENV
   : '\\end{align}'
   ;

ALIGNAT_ENV
   : '\\begin{alignat}'
   ;

END_ALIGNAT_ENV
   : '\\end{alignat}'
   ;

FLALIGN_ENV
   : '\\begin{flalign}'
   ;

END_FLALIGN_ENV
   : '\\end{flalign}'
   ;

SUBARRAY_ENV
   : '\\begin{subarray}'
   ;

END_SUBARRAY_ENV
   : '\\end{subarray}'
   ;

OPERATOR_NAME_CMD
   : '\\operatorname'
   ;

MATHOP_CMD
   : '\\mathop'
   ;

MATHACCENT_CMD
   : '\\mathaccent'
   ;

MATHACCENT_V_CMD
   : '\\mathaccentV'
   ;

MATHALPHA_CMD
   : '\\mathalpha'
   ;

MATHBIN_CMD
   : '\\mathbin'
   ;

MATHCHAR_CMD
   : '\\mathchar'
   ;

MATHCHARDELIM_CMD
   : '\\mathchardelim'
   ;

MATHCODE_CMD
   : '\\mathcode'
   ;

MATHINNER_CMD
   : '\\mathinner'
   ;

MATHOPEN_CMD
   : '\\mathopen'
   ;

MATHORD_CMD
   : '\\mathord'
   ;

MATHPUNCT_CMD
   : '\\mathpunct'
   ;

MATHREL_CMD
   : '\\mathrel'
   ;

MATHRING_CMD
   : '\\mathring'
   ;

MATHSURROUND_CMD
   : '\\mathsurround'
   ;

LEFT_CMD
   : '\\left'
   ;

RIGHT_CMD
   : '\\right'
   ;

BIG_CMD
   : '\\big'
   ;

BIGL_CMD
   : '\\bigl'
   ;

BIGR_CMD
   : '\\bigr'
   ;

BIGG_CMD
   : '\\bigg'
   ;

BIGGL_CMD
   : '\\biggl'
   ;

BIGGR_CMD
   : '\\biggr'
   ;

LVERT_CMD
   : '\\lvert'
   ;

RVERT_CMD
   : '\\rvert'
   ;

LVERT_NORM_CMD
   : '\\lVert'
   ;

RVERT_NORM_CMD
   : '\\rVert'
   ;

LANGLE_CMD
   : '\\langle'
   ;

RANGLE_CMD
   : '\\rangle'
   ;

THINSPACE
   : '\\thinspace'
   ;

MEDSPACE
   : '\\medspace'
   ;

THICKSPACE
   : '\\thickspace'
   ;

NEGTHINSPACE
   : '\\negthinspace'
   ;

NEGMEDSPACE
   : '\\negmedspace'
   ;

NEGTHICKSPACE
   : '\\negthickspace'
   ;

MSPACE
   : '\\mspace'
   ;

KERN
   : '\\kern'
   ;

HSPACE
   : '\\hspace'
   ;

QQUAD
   : '\\qquad'
   ;

QUAD
   : '\\quad'
   ;

BEGIN_GROUP_CMD
   : '\\begingroup'
   ;

END_GROUP_CMD
   : '\\endgroup'
   ;

B_GROUP_CMD
   : '\\bgroup'
   ;

E_GROUP_CMD
   : '\\egroup'
   ;

NONUMBER
   : '\\nonumber'
   ;

TAG_CMD
   : '\\tag'
   ;

TAG_STAR_CMD
   : '\\tag*'
   ;

INTERTEXT
   : '\\intertext'
   ;

DISPLAYBREAK
   : '\\displaybreak'
   ;

ALLOWDISPLAYBREAKS
   : '\\allowdisplaybreaks'
   ;

NOBREAKDASH
   : '\\nobreakdash'
   ;

RAISETAG
   : '\\raisetag'
   ;

NOLIMITS
   : '\\nolimits'
   ;

LIMITS
   : '\\limits'
   ;

DISPLAYLIMITS
   : '\\displaylimits'
   ;

SMASH
   : '\\smash'
   ;

HFDOTSFOR
   : '\\hdotsfor'
   ;

MATHOP_DECL_CMD
   : '\\DeclareMathOperator'
   ;

MATHOP_DECL_STAR_CMD
   : '\\DeclareMathOperator*'
   ;

OVER_CMD
   : '\\over'
   ;

OVERWITHDELIMS_CMD
   : '\\overwithdelims'
   ;

ATOP_CMD
   : '\\atop'
   ;

ATOPWITHDELIMS_CMD
   : '\\atopwithdelims'
   ;

ABOVE_CMD
   : '\\above'
   ;

ABOVEWITHDELIMS_CMD
   : '\\abovewithdelims'
   ;

CFRAC
   : '\\cfrac'
   ;

SHOVELEFT
   : '\\shoveleft'
   ;

SHOVERIGHT
   : '\\shoveright'
   ;

MATHSTYLE
   : '\\mathstyle'
   ;

MATHCHOICE
   : '\\mathchoice'
   ;

IF_M_MODE
   : '\\ifmmode'
   ;

IF_DISPLAY_MODE
   : '\\ifdisplay'
   ;

IF_INNER_MODE
   : '\\ifinner'
   ;

FORALL
   : '\\forall'
   ;

EXISTS
   : '\\exists'
   ;

IMPLIES
   : '\\implies'
   ;

MAPSTO
   : '\\mapsto'
   ;

LEFTARROW
   : '\\leftarrow'
   ;

RIGHTARROW
   : '\\rightarrow'
   ;

LEFTrightarrow
   : '\\leftrightarrow'
   ;

LE
   : '\\le'
   ;

LEQ
   : '\\leq'
   ;

GE
   : '\\ge'
   ;

GEQ
   : '\\geq'
   ;

NEQ
   : '\\neq'
   ;

APPROX
   : '\\approx'
   ;

IN
   : '\\in'
   ;

SUBSET_EQ
   : '\\subseteq'
   ;

UNION
   : '\\cup'
   ;

INTERSECTION
   : '\\cap'
   ;

EMPTYSET
   : '\\emptyset'
   ;

NATURAL_NUMBERS
   : '\\mathbb{N}'
   ;

INTEGERS
   : '\\mathbb{Z}'
   ;

RATIONALS
   : '\\mathbb{Q}'
   ;

REALS
   : '\\mathbb{R}'
   ;

COMPLEX
   : '\\mathbb{C}'
   ;

ALEPH
   : '\\aleph'
   ;

ABSTRACT_ENV
   : '\\begin{abstract}'
   ; // Added environments
   
END_ABSTRACT_ENV
   : '\\end{abstract}'
   ;

ARRAY_ENV
   : '\\begin{array}'
   ;

END_ARRAY_ENV
   : '\\end{array}'
   ;

CENTER_ENV
   : '\\begin{center}'
   ;

END_CENTER_ENV
   : '\\end{center}'
   ;

DOCUMENT_ENV
   : '\\begin{document}'
   ;

END_DOCUMENT_ENV
   : '\\end{document}'
   ;

ENUMERATE_ENV
   : '\\begin{enumerate}'
   ;

END_ENUMERATE_ENV
   : '\\end{enumerate}'
   ;

EQNARRAY_ENV_UNSTARRED
   : '\\begin{eqnarray}'
   ; // To differentiate from EQNARRAY_ENV_STAR
   
END_EQNARRAY_ENV_UNSTARRED
   : '\\end{eqnarray}'
   ;

EQUATION_ENV_UNSTARRED
   : '\\begin{equation}'
   ; // To differentiate from EQUATION_ENV_STAR
   
END_EQUATION_ENV_UNSTARRED
   : '\\end{equation}'
   ;

FIGURE_ENV_UNSTARRED
   : '\\begin{figure}'
   ; // To differentiate from FIGURE_ENV_STAR
   
END_FIGURE_ENV_UNSTARRED
   : '\\end{figure}'
   ;

ITEMIZE_ENV
   : '\\begin{itemize}'
   ;

END_ITEMIZE_ENV
   : '\\end{itemize}'
   ;

LEMMA_ENV
   : '\\begin{lemma}'
   ;

END_LEMMA_ENV
   : '\\end{lemma}'
   ;

LSTLISTING_ENV
   : '\\begin{lstlisting}'
   ;

END_LSTLISTING_ENV
   : '\\end{lstlisting}'
   ;

MINIPAGE_ENV
   : '\\begin{minipage}'
   ;

END_MINIPAGE_ENV
   : '\\end{minipage}'
   ;

PROOF_ENV
   : '\\begin{proof}'
   ;

END_PROOF_ENV
   : '\\end{proof}'
   ;

TABLE_ENV
   : '\\begin{table}'
   ;

END_TABLE_ENV
   : '\\end{table}'
   ;

TABULAR_ENV
   : '\\begin{tabular}'
   ;

END_TABULAR_ENV
   : '\\end{tabular}'
   ;

THEBIBLIOGRAPHY_ENV
   : '\\begin{thebibliography}'
   ;

END_THEBIBLIOGRAPHY_ENV
   : '\\end{thebibliography}'
   ;

THEOREM_ENV
   : '\\begin{theorem}'
   ;

END_THEOREM_ENV
   : '\\end{theorem}'
   ;
   // Tokens from the original LaTeXLexer (for completeness and if still needed) - No changes needed here, names are ok
   
VARIABLE
   : [a-zA-Z]
   ;

PI
   : '\\pi'
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

POW
   : '^'
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

DIVIDE_OP
   : '/'
   ;

EQUALS
   : '='
   ;

FLOAT
   : INTEGER ('.' INTEGER)?
   ;

INTEGER
   : ZERO
   | DIGIT_NON_ZERO DIGIT*
   ;

SYMBOL_GENERIC
   : '\\' [a-zA-Z]+
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

