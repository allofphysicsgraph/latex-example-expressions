#!/usr/bin/env python3
import json
import glob

#import random
from subprocess import PIPE  # https://docs.python.org/3/library/subprocess.html
import subprocess  # https://stackoverflow.com/questions/39187886/what-is-the-difference-between-subprocess-popen-and-subprocess-run/39187984


proc_timeout = 30

def compile_tex_to_dvi(file_name: str) -> None:
    process = subprocess.run(
        ["latex", "-halt-on-error", file_name + ".tex"],
        stdout=PIPE,
        stderr=PIPE,
        timeout=proc_timeout,
    )
    # latex_stdout, latex_stderr = process.communicate()
    # https://stackoverflow.com/questions/41171791/how-to-suppress-or-capture-the-output-of-subprocess-run
    latex_stdout = process.stdout.decode("utf-8")
    print(latex_stdout)
    latex_stderr = process.stderr.decode("utf-8")
    print(latex_stderr)
    return

def dvi_to_pdf(file_name: str) -> None:
    # https://tex.stackexchange.com/questions/73783/dvipdfm-or-dvipdfmx-or-dvipdft
    process = subprocess.run(
        ["dvipdfmx", file_name + ".dvi"],
        stdout=PIPE,
        stderr=PIPE,
        timeout=proc_timeout,
    )

    dvipdf_stdout = process.stdout.decode("utf-8")
    print(dvipdf_stdout)
    dvipdf_stderr = process.stderr.decode("utf-8")
    print(dvipdf_stderr)
    return

def create_latex_file(file_name: str, math_latex: str):
    """
    >>> create_latex_file('a_file_name', 'a=b') 
    """
    with open(file_name + ".tex", "w") as lat_file:
        lat_file.write("\\documentclass[12pt]{article}\n")
        lat_file.write("\\thispagestyle{empty}\n")
        lat_file.write("\\usepackage{amsmath}\n")

        lat_file.write("\\begin{document}\n")
        #lat_file.write("\\begin{equation}\n")

        lat_file.write(math_latex + "\n")

        #lat_file.write("\\end{equation}\n")
        lat_file.write("\\end{document}\n")
    return


def compile_main_to_pdf(folder_with_valid_latex: str)->None:
    # copy contents
    with open(folder_with_valid_latex+"main.tex","r") as file_handle:
        file_content = file_handle.read()
    with open("main.tex","w") as file_handle:
        file_handle.write(file_content)
    compile_tex_to_dvi("main")
    dvi_to_pdf("main")

def compile_each_example_to_pdf(folder_with_valid_latex: str)->None:
    list_of_latex_expressions = glob.glob(folder_with_valid_latex+"expression_*.tex")

    print("list_of_latex_expressions=",list_of_latex_expressions)

    for latex_expr_filename in list_of_latex_expressions:
        with open(latex_expr_filename,'r') as file_handle:
            file_content = file_handle.read()

        print(file_content)
        file_name = latex_expr_filename.replace(".tex","")
        file_name = file_name.replace(folder_with_valid_latex,"")
        print("file_name=",file_name)

        create_latex_file(file_name, file_content)
        compile_tex_to_dvi(file_name)
        dvi_to_pdf(file_name)



if __name__ == "__main__":
    folder_with_valid_latex = "/scratch/examples_of_valid_latex/"

    compile_main_to_pdf(folder_with_valid_latex)
    compile_each_example_to_pdf(folder_with_valid_latex)
