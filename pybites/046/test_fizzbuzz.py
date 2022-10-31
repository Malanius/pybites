from fizzbuzz import fizzbuzz


def test_fizzbuzz_not_divisible_by_3_or_5():
    numbers = [number for number in range(1, 100) if number % 3 != 0 and number % 5 != 0]
    for number in numbers:
        assert fizzbuzz(number) == number


def test_fizzbuzz_dibisible_by_3():
    numbers = [number for number in range(1, 100) if number % 3 == 0 and number % 5 != 0]
    for number in numbers:
        assert fizzbuzz(number) == "Fizz"


def test_fizzbuzz_divisible_by_5():
    numbers = [number for number in range(1, 100) if number % 5 == 0 and number % 3 != 0]
    for number in numbers:
        assert fizzbuzz(number) == "Buzz"


def test_fizzbuzz_divisible_by_3_and_5():
    numbers = [
        number for number in range(1, 100) if number % 3 == 0 and number % 5 == 0
    ]
    for number in numbers:
        assert fizzbuzz(number) == "Fizz Buzz"
