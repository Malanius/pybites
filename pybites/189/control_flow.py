from typing import List


IGNORE_CHAR = "b"
QUIT_CHAR = "q"
MAX_NAMES = 5


def filter_names(names: List[str]) -> List[str]:
    filtered_names = []
    for name in names:
        if name.startswith(IGNORE_CHAR):
            continue
        if any(char.isdigit() for char in name):
            continue
        if name.startswith(QUIT_CHAR):
            break
        if len(filtered_names) < MAX_NAMES:
            filtered_names.append(name)
    return filtered_names
