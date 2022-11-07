import re


def strip_hastag_lines(code):
    return re.sub(r"^\s*#.*$\n", "", code, flags=re.MULTILINE)


def strip_hastag_inline(code):
    return re.sub(r"\s{2,}#.*$", "", code, flags=re.MULTILINE)


def strip_docstrings(code):
    return re.sub(r' *""".*?"""\n', "", code, flags=re.DOTALL)


def strip_comments(code):
    code = strip_hastag_lines(code)
    code = strip_hastag_inline(code)
    code = strip_docstrings(code)
    return code
