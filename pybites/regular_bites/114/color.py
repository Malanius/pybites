import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, "color_values.py")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/color_values.py", color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.rgb = COLOR_NAMES.get(color.upper())
        self.color = color

    @staticmethod
    def is_valid_hex(hex):
        """Class method that checks if a hex value is valid"""
        return isinstance(hex, str) and hex.startswith("#") and len(hex) == 7

    @staticmethod
    def hex2rgb(hex):
        """Class method that converts a hex value into an rgb one"""
        if not Color.is_valid_hex(hex):
            raise ValueError
        # courtesy of https://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa
        hex = hex.lstrip("#")
        hex_length = len(hex)
        return tuple(
            int(hex[i : i + hex_length // 3], 16)
            for i in range(0, hex_length, hex_length // 3)
        )

    @staticmethod
    def is_valid_rgb(rgb):
        """Class method that checks if a rgb value is valid"""
        return (
            isinstance(rgb, tuple)
            and len(rgb) == 3
            and all(isinstance(value, int) and 0 <= value <= 255 for value in rgb)
        )

    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        if not Color.is_valid_rgb(rgb):
            raise ValueError
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        rgb = COLOR_NAMES.get(self.color.upper())
        return f"({rgb[0]}, {rgb[1]}, {rgb[2]})" if rgb else "Unknown"
