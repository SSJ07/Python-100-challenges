"""
Sum of number recursively
"""
from functools import reduce


def calc_sum(n: int) -> int:
    """
    Calculate sum of all numbers in given range
    :param n: Input number
    :return: sum of all numbers
    """
    total: int = 0
    for i in range(1, n + 1):
        total += i
    return total


def calc_sum_with_recursion(n: int) -> int:
    return n if n == 1 else (n + calc_sum_with_recursion(n - 1))


def calc_sum_with_reduce(n: int) -> int:
    if n == 1:
        return 1
    return reduce(lambda n, n_1: n + n_1, range(1, n + 1))


sum_of_numbers = lambda n: n + sum_of_numbers(n - 1) if n > 1 else 1

optimized_sum = lambda n: (n * (n + 1)) // 2
