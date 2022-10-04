def get_index_different_char(chars: list) -> int:
    alfanumerics = [c for c in chars if str(c).isalnum()]
    non_alfanumerics = [c for c in chars if not str(c).isalnum()]

    if len(alfanumerics) > len(non_alfanumerics):
        return chars.index(non_alfanumerics[0])

    return chars.index(alfanumerics[0])
