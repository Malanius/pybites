def rotate(string: str, n: int) -> str:
    """Rotate characters in a string.
    Expects string and n (int) for number of characters to move.
    """
    return string[n:] + string[:n]
