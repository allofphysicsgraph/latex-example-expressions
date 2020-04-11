# latex_tests
test of latex

    docker build -t 'lat' .
    docker run -it --rm lat:latest /bin/bash
    python generate_latex_files.py

This is in support of https://github.com/sympy/sympy/issues/19075
and https://github.com/allofphysicsgraph/proofofconcept/issues/79

For the comprehensive list of Latex symbols, see
http://mirror.utexas.edu/ctan/info/symbols/comprehensive/symbols-a4.pdf
and
http://ctan.math.illinois.edu/info/symbols/comprehensive/source/symbols.tex

for AMSmath, see
https://texdoc.net/texmf-dist/doc/latex/amsmath/amsldoc.pdf

