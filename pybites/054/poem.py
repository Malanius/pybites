import re
import textwrap

INDENTS = 4


def print_hanging_indents(poem: str) -> None:
    """Receives a multiline poem and prints it with hanging indents"""
    parts = poem.split("\n\n")
    for part in parts:
        cleaned = re.sub(r"^\s+", "", part, flags=re.MULTILINE)
        print(textwrap.indent(cleaned, " " * INDENTS).strip())
