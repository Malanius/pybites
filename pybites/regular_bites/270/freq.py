from collections import Counter


def freq_digit(num: int) -> int:
    count = Counter(str(num))
    most_common = count.most_common(1)[0][0]
    return int(most_common)
