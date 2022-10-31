import itertools as it


def find_number_pairs(numbers, N=10):
    adds_to_N = []
    for pair in it.combinations(numbers, 2):
        if sum(pair) == N:
            adds_to_N.append(pair)

    return adds_to_N
