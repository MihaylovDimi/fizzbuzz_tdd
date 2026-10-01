"""FizzBuzz production code, written only to make failing tests pass."""


def fizzbuzz(n):
    """Return "Fizz", "Buzz", "FizzBuzz" or the number itself as a string."""
    divisible_by_3 = n % 3 == 0
    divisible_by_5 = n % 5 == 0

    if divisible_by_3 and divisible_by_5:
        return "FizzBuzz"
    if divisible_by_3:
        return "Fizz"
    if divisible_by_5:
        return "Buzz"
    return str(n)
