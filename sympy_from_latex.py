#!/usr/bin/env python3

"""
This file was informed by
https://github.com/allofphysicsgraph/sympy-in-docker/blob/main/eval_latex.py

run this file using
docker run -it --rm -v `pwd`:/scratch --workdir /scratch sympyonubuntu python3 sympy_from_latex.py
"""

import glob

import sympy
print("sympy:",sympy.__version__)

from sympy.parsing.latex import parse_latex

from sympy.core.sympify import SympifyError

from sympy.parsing.latex.errors import LaTeXParsingError

category = "cleaned"
#category = "expression"

write_results_to_file = False

parse_success_count = 0
parse_fail_count = 0

if __name__ == "__main__":
    folder_with_valid_latex = "examples_of_valid_latex/"

    list_of_latex_expression_files = glob.glob(folder_with_valid_latex+"*_"+category+"_latex.tex")

    #print("list_of_latex_expressions=",list_of_latex_expression_files)

    for this_latex_expression_path_filename in list_of_latex_expression_files:

        this_latex_expression_filename = this_latex_expression_path_filename.split("/")[1]

        this_filename_no_extension = this_latex_expression_filename.replace(".tex","")

        print("\n"+this_filename_no_extension)
        prefix = this_filename_no_extension.split("_")[0]
        #print("prefix",prefix)

        with open(this_latex_expression_path_filename,"r") as file_handle:
            file_content = file_handle.read()

        file_content =file_content.replace("\\begin{equation}","").replace("\\end{equation}","").strip()

        print("raw Latex:\n",file_content,"\n")

        expr_error = False
        expr = None
        err = None
        try:
            expr = parse_latex(file_content)
            parse_success_count+=1
        except LaTeXParsingError as err:
            expr_error = True
            parse_fail_count+=1
            print("ERROR: sympy.parsing.latex.errors.LaTeXParsingError")
            print(err)
            error_message = str(err)
        except TypeError as err:
            expr_error = True
            parse_fail_count+=1
            print("ERROR: TypeError")
            print(err)
            error_message = str(err)
        except SympifyError as err:
            expr_error = True
            parse_fail_count+=1
            print("ERROR: sympy.core.sympify.SympifyError")
            print(err)
            error_message = str(err)


        # if not expr_error:
        #     #print("type:",type(expr))
        #     print("\\begin{verbatim}")
        #     print(str(expr))
        #     print("\\end{verbatim}")
        #     if write_results_to_file:
        #         with open(folder_with_valid_latex+prefix+"_"+category+"_latex_sympy_112_antlr4-python3-runtime411_expression.tex","w") as file_handle:
        #             file_handle.write("\\begin{verbatim}\n")
        #             file_handle.write(str(expr))
        #             file_handle.write("\n\\end{verbatim}\n")

        #     print("atoms:")
        #     atoms = str(expr.atoms())
        #     #atoms = atoms.replace("\\","\\\\")
        #     print("$"+atoms+"$")
        #     #print("using antlr4-python3-runtime==4.11 and sympy==1.12")
        #     if write_results_to_file:
        #         with open(folder_with_valid_latex+prefix+"_"+category+"_latex_sympy_112_antlr4-python3-runtime411_atoms.tex","w") as file_handle:
        #             file_handle.write("$"+atoms+"$")
        # else: # error in SymPy parsing of Latex
        #     if write_results_to_file:
        #         with open(folder_with_valid_latex+prefix+"_"+category+"_latex_sympy_112_antlr4-python3-runtime411_expression.tex","w") as file_handle:
        #             file_handle.write("\\begin{verbatim}\n")
        #             file_handle.write(str(error_message))
        #             file_handle.write("\n\\end{verbatim}\n")

print("parse_success_count =",parse_success_count)
print("parse_fail_count =",parse_fail_count)

#EOF