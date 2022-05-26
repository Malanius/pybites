def is_armstrong(n: int) -> bool:
    n_str = str(n)
    num_digits = len(n_str)
    digits = [int(digit) for digit in n_str]
    pow_digits = [digit**num_digits for digit in digits]
    return sum(pow_digits) == n
