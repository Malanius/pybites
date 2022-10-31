from pathlib import Path
from typing import List


def tail(filepath: Path, n: int) -> List[str]:
    """
    Similate Unix' "tail -n" command:
    - Read in the file ("filepath").
    - Parse it into a list of lines, stripping trailing newlines.
    - Return the last "n" lines.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.rstrip() for line in lines[-n:]]