from typing import Tuple


def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
    boundaries (0, 255) and returns its converted hex, for example:
    Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if not all(0 <= x <= 255 for x in rgb):
        raise ValueError
    return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"
