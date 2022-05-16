from posixpath import split


MESSAGE = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""


def split_in_columns(message: str = MESSAGE):
    """Split the message by newline (\n) and join it together on '|'
    (pipe), return the obtained output string"""
    splitted = message.split("\n")
    joinded = "|".join(splitted)
    return joinded
