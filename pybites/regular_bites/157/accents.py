import unicodedata


def filter_accents(text: str):
    """Return a sequence of accented characters found in
    the passed in lowercased text string
    """
    return [c for c in text.lower() if unicodedata.decomposition(c) != ""]
