import re

PUNCT = re.compile(r'[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]+')

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return PUNCT.sub('', input_string)