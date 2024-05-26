#!/usr/bin/env python3

"""
clean latex expressions
"""

import glob

from lib_clean_latex_string import remove_latex_presention_markings


if __name__ == "__main__":
    folder_with_valid_latex = "examples_of_valid_latex/"

    list_of_latex_expression_files = glob.glob(folder_with_valid_latex+"*_expression_latex.tex")

    #print("list_of_latex_expressions=",list_of_latex_expression_files)

    for this_latex_expression_path_filename in list_of_latex_expression_files:

        this_latex_expression_filename = this_latex_expression_path_filename.split("/")[1]

        this_filename_no_extension = this_latex_expression_filename.replace(".tex","")

        print("\n"+this_filename_no_extension)
        prefix = this_filename_no_extension.split("_")[0]
        #print("prefix",prefix)


        with open(this_latex_expression_path_filename,'r') as file_handle:
            file_content_raw_latex = file_handle.read()
        print("raw Latex:")
        print(file_content_raw_latex)

        cleaned_latex = remove_latex_presention_markings(file_content_raw_latex)

        print("cleaned Latex:")
        print(cleaned_latex)

        with open(folder_with_valid_latex+prefix+"_cleaned_latex.tex",'w') as file_handle:
        	file_handle.write(cleaned_latex)
        	