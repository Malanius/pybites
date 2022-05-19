from string import ascii_lowercase

TEXT = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""


def slice_and_dice(text: str = TEXT) -> list:
    """Get a list of words from the passed in text.
    See the Bite description for step by step instructions"""
    results = []

    # Take the block of text provided and strip off the whitespace at both ends.
    text.strip()
    # Split the text by newline (\n).
    lines = text.split("\n")
    
    # Loop through the lines, for each line:
    for line in lines:
        # strip off any leading spaces
        clean_line = line.strip()
        # check if the first character is lowercase
        if not clean_line[:1].islower():
            continue

        # if so, split the line into words and get the last word,
        last_word = clean_line.split()[-1]
        # strip off BOTH the trailing dot (.) and exclamation mark (!) from this last word
        clean_word = last_word.replace(".", "").replace("!", "")
        # and finally add it to the results list.
        results.append(clean_word)

    return results
