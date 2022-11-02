import textwrap
import itertools as it

COL_WIDTH = 20


def text_to_columns(text: str) -> str:
    """Split text (input arg) to columns, the amount of double
    newlines (\n\n) in text determines the amount of columns.
    Return a string with the column output like:
    line1\nline2\nline3\n ... etc ...
    See also the tests for more info."""
    columns = text.split("\n\n")
    columns_text = []
    for col in columns:
        columns_text.append(textwrap.wrap(col.strip(), width=COL_WIDTH))

    print(columns_text)

    final_string = ""
    zipped = list(it.zip_longest(*columns_text, fillvalue=""))

    for line_tuple in zipped:
        final_string += "\t".join(line_tuple)

    return final_string
