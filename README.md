
![alt text](https://raw.githubusercontent.com/allofphysicsgraph/latex-example-expressions/master/decision_tree.png)

Explanation of files in this repo:

# manually created files

The folder `examples_of_valid_latex` contains manually created valid Latex expressions, one per file:
`examples_of_valid_latex/*_expression_latex.tex`

For each Latex expression there's also a manually created set of expected symbols:
`examples_of_valid_latex/*_expected_tokens.tex`

TODO: complete the manual specification of expected symbols.

# aggregation file

The file `examples_of_valid_latex/main.tex` aggregates all the other `*.tex` files into one PDF that a user can then manually review. (`main.tex` was partially generated by `generate_main.py`.)

# generated file content

## raw Latex expression parsed using SymPy 1.12 with antlr4-python3-runtime 4.11

The content for each file 
`examples_of_valid_latex/*_expression_latex_sympy_112_antlr4-python3-runtime411_expression.tex`
was generated using 
```bash
docker run -it --rm -v `pwd`:/scratch --workdir /scratch sympyonubuntu python3 sympy_from_latex.py
```

Similarly, the content for each file 
`examples_of_valid_latex/*_expression_latex_sympy_112_antlr4-python3-runtime411_atoms.tex`
also comes from that same `.py` script.

## clean Latex expression parsed using SymPy 1.12 with antlr4-python3-runtime 4.11

Sometimes the reason SymPy fails to parse successfully is due to presentation-related spacing. 
By removing the non-essential spacing marks, SymPy is more likely to succeed.

The file
`examples_of_valid_latex/*_cleaned_latex.tex`
is the cleaned version of
`examples_of_valid_latex/*_expression_latex.tex`

The command used was 
```bash
python3 clean_latex_expressions.py
```

Then SymPy 1.12 with antlr4-python3-runtime 4.11 is used on
`examples_of_valid_latex/*_cleaned_latex.tex`
to generate
`examples_of_valid_latex/*_cleaned_latex_sympy_112_antlr4-python3-runtime411_expression.tex`
and
`examples_of_valid_latex/*_cleaned_latex_sympy_112_antlr4-python3-runtime411_atoms.tex`

The command is
```bash
docker run -it --rm -v `pwd`:/scratch --workdir /scratch sympyonubuntu python3 sympy_from_latex.py
```

That docker image is from <https://github.com/allofphysicsgraph/sympy-in-docker/tree/main>	


# context

This repo content is related to <https://github.com/sympy/sympy/issues/19075>
and <https://github.com/allofphysicsgraph/proofofconcept/issues/79>

For the comprehensive list of Latex symbols, see
<http://mirror.utexas.edu/ctan/info/symbols/comprehensive/symbols-a4.pdf>
and
<http://ctan.math.illinois.edu/info/symbols/comprehensive/source/symbols.tex>

for AMSmath, see
<https://texdoc.net/texmf-dist/doc/latex/amsmath/amsldoc.pdf>

