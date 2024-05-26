#!/usr/bin/env python3


def remove_latex_presention_markings(latex_str: str) -> str:
    """
    This function is from
    https://github.com/allofphysicsgraph/ui_v8_website_flask_neo4j/blob/gh-pages/webserver/library/compute.py

    clean the latex string

    based on the struggle with spacing,
    https://github.com/sympy/sympy/issues/19075#issuecomment-633643570
    BHP realized removing the presentation-related aspects would make the task for Sympy easier

    >>> remove_latex_presention_markings('a\\ b = c')
    'a b = c'
    """
    # trace_id = str(random.randint(1000000, 9999999))
    # print("[TRACE] func: compute/remove_latex_presention_markings start " + trace_id)

    # print("latex to be cleaned: " + latex_str)

    if "\\left." in latex_str:
        latex_str = latex_str.replace("\\left.", "")
    if "\\right." in latex_str:
        latex_str = latex_str.replace("\\right.", "")
    if "\\left|" in latex_str:
        latex_str = latex_str.replace("\\left|", "|")
    if "\\right|" in latex_str:
        latex_str = latex_str.replace("\\right|", "|")
    if "\\left(" in latex_str:
        latex_str = latex_str.replace("\\left(", "(")
    if "\\right)" in latex_str:
        latex_str = latex_str.replace("\\right)", ")")
    if "\\," in latex_str:
        # logger.debug("found space \\,")
        latex_str = latex_str.replace("\\,", " ")  # thinspace
    if "\\ " in latex_str:
        # logger.debug("found space \\ ")
        latex_str = latex_str.replace("\\ ", " ")
    if "\\;" in latex_str:
        # logger.debug("found space \\;")
        latex_str = latex_str.replace("\\;", " ")  # thick space
    if "\\:" in latex_str:
        # logger.debug("found space \\:")
        latex_str = latex_str.replace("\\:", " ")  # medium space
    if "\\!" in latex_str:
        # logger.debug("found space \\!")
        latex_str = latex_str.replace("\\!", " ")  # negative space
    if "\\;" in latex_str:
        # logger.debug("found space \\ ")
        latex_str = latex_str.replace("\\ ", " ")
    if "\\quad" in latex_str:
        # logger.debug("found space \\quad")
        latex_str = latex_str.replace("\\quad", " ")
    if "\\qquad" in latex_str:
        # logger.debug("found space \\qquad")
        latex_str = latex_str.replace("\\qquad", " ")

    # print("latex after cleaning: " + latex_str)

    # print("[TRACE] func: compute/remove_latex_presention_markings end " + trace_id)
    return latex_str

if __name__ == "__main__":
    print("this is just a library")
