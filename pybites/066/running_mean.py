import itertools as it


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
    returns a sequence of same length with the averages.
    You can assume all items in sequence are numeric."""
    for i, num in enumerate(it.accumulate(sequence), start=1):
        yield round(num / i, 2)