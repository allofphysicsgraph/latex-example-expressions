#!/usr/bin/env python3

"""
BHP wrote this as a one-time script on 2024-05-25 
and doesn't expect to re-use this content.
"""

import glob

list_of_filenames = glob.glob("*.tex")

#print("list_of_filenames",list_of_filenames)

with open("main.tex",'w') as file_handle_main:

	for this_filename in list_of_filenames:
		this_filename_no_extension = this_filename.replace(".tex","")
		#print(this_filename_no_extension)
		prefix = this_filename_no_extension.split("_")[0]
		print(prefix)

		file_handle_main.write("\input{"+prefix+"_expression_latex"+"}\n")
		# with open(prefix+"_cleaned_latex_sympy_112_antlr4-python3-runtime411_expression"+".tex","w") as file_handle:
		# 	file_handle.write("\n")
		file_handle_main.write("parses to\n")
		file_handle_main.write("\input{"+prefix+"_cleaned_latex_sympy_112_antlr4-python3-runtime411_expression"+"}\n")
		

		file_handle_main.write("with atoms\n")
		# with open(prefix+"_cleaned_latex_sympy_112_antlr4-python3-runtime411_atoms"+".tex","w") as file_handle:
		# 	file_handle.write("\n")
		file_handle_main.write("\input{"+prefix+"_cleaned_latex_sympy_112_antlr4-python3-runtime411_atoms"+"}\\\\\n")
		file_handle_main.write("using antlr4-python3-runtime==4.11 and sympy==1.12\n")
		file_handle_main.write("\n")
		file_handle_main.write("\\ \\\\\n")
		file_handle_main.write("cleaned \LaTeX\n")
		# with open(prefix+"_cleaned_latex"+".tex","w") as file_handle:
		# 	file_handle.write("\n")
		file_handle_main.write("\input{"+prefix+"_cleaned_latex"+"}\n")
		file_handle_main.write("parses to\n")
		# with open(prefix+"_expression_latex_sympy_112_antlr4-python3-runtime411_expression"+".tex","w") as file_handle:
		# 	file_handle.write("\n")
		file_handle_main.write("\input{"+prefix+"_expression_latex_sympy_112_antlr4-python3-runtime411_expression"+"}\n")
		file_handle_main.write("with atoms\n")
		# with open(prefix+"_expression_latex_sympy_112_antlr4-python3-runtime411_atoms"+".tex","w") as file_handle:
		# 	file_handle.write("\n")
		file_handle_main.write("\input{"+prefix+"_expression_latex_sympy_112_antlr4-python3-runtime411_atoms"+"}\n")
		file_handle_main.write("\n")
		file_handle_main.write("\\ \\\\\n")
		file_handle_main.write("Expected tokens:\n")
		# with open(prefix+"_expected_tokens"+".tex","w") as file_handle:
		# 	file_handle.write("\n")
		file_handle_main.write("\input{"+prefix+"_expected_tokens"+"}\n\n")
		file_handle_main.write("\\hrulefill\n")

