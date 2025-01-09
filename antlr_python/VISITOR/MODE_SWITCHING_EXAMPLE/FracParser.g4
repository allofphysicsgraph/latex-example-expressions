parser grammar FracParser;
options { tokenVocab=FracLexer; }
expr:
    frac+
    ;
frac:
    FRAC numerator denominator;

numerator:
    SINGLE_DIGIT;

denominator:
    SINGLE_DIGIT_NON_ZERO;

