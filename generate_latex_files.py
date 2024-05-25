#!/usr/bin/env python3
import json

#import random
from subprocess import PIPE  # https://docs.python.org/3/library/subprocess.html
import subprocess  # https://stackoverflow.com/questions/39187886/what-is-the-difference-between-subprocess-popen-and-subprocess-run/39187984


proc_timeout = 30

def compile_tex_to_dvi(file_name):
    process = subprocess.run(
        ["latex", "-halt-on-error", file_name + ".tex"],
        stdout=PIPE,
        stderr=PIPE,
        timeout=proc_timeout,
    )
    # latex_stdout, latex_stderr = process.communicate()
    # https://stackoverflow.com/questions/41171791/how-to-suppress-or-capture-the-output-of-subprocess-run
    latex_stdout = process.stdout.decode("utf-8")
    latex_stderr = process.stderr.decode("utf-8")
    return

def dvi_to_pdf(file_name):
    # https://tex.stackexchange.com/questions/73783/dvipdfm-or-dvipdfmx-or-dvipdft
    process = subprocess.run(
        ["dvipdfmx", file_name + ".dvi"],
        stdout=PIPE,
        stderr=PIPE,
        timeout=proc_timeout,
    )

    dvipdf_stdout = process.stdout.decode("utf-8")
    dvipdf_stderr = process.stderr.decode("utf-8")
    return

def create_latex_file(file_name, math_latex):
    """
    >>> runme() 
    """
    with open(file_name + ".tex", "w") as lat_file:
        lat_file.write("\\documentclass[12pt]{article}\n")
        lat_file.write("\\thispagestyle{empty}\n")

        lat_file.write("\\begin{document}\n")
        lat_file.write("\\begin{equation}\n")

        lat_file.write(math_latex + "\n")

        lat_file.write("\\end{equation}\n")
        lat_file.write("\\end{document}\n")
    return


def check_list_of_latex(list_of_latex):
    file_indx = 9

    list_of_failed_latex = []
    for this_latex in list_of_latex:
        file_indx += 1
        print('\nfile',str(file_indx),'contains\n', this_latex, '\n')
        file_name = str(file_indx)
        create_latex_file(file_name, this_latex)
        compile_tex_to_dvi(file_name)
        dvi_to_pdf(file_name)

    return list_of_failed_latex

if __name__ == "__main__":

    check_list_of_latex(list_of_latex)

