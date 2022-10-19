import itertools as it
import string


def sequence_generator():
    alphabet = it.cycle(string.ascii_uppercase)
    numbers = it.cycle(range(1, 27))
    yield from it.chain.from_iterable(zip(numbers, alphabet))
