lexer grammar FracLexer;

FRAC: '\\frac' -> mode(NUMERATOR);

mode NUMERATOR;
SINGLE_DIGIT: [0-9]-> mode(DENOMINATOR);

mode DENOMINATOR;
SINGLE_DIGIT_NON_ZERO: [1-9] -> mode(DEFAULT_MODE);
