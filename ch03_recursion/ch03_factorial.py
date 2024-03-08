"""
Factorial

5! = 5 * 4 * 3 * 2 * 1 = 120

There are multiple ways to calculate factorial:
    1. Normal loop
    2. Recursive way
    3. Python shortcut(using lambda)
    4. Using reduce function
"""
from functools import reduce


# 1. Normal loop
def calc_factorial_with_normal_loop(num: int) -> int:
    """
    Calculate factorial number for given value.
    :param num: Input value
    :return: Factorial of given number
    """
    fact: int = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact


# 2. Recursive way
def calc_factorial_with_recursion(value: int) -> int:
    if value < 0:
        raise Exception("Value must be greater than 0")

    if value == 1 or value == 0:
        return 1

    return value * calc_factorial_with_normal_loop(value - 1)


# 3. Python shortcut(using lambda)
factorial = lambda n: n * factorial(n - 1) if n >= 1 else 1


# 4. Using reduce function
def calc_factorial_with_reduce(value: int) -> int:
    """
    Calculate factorial using reduce function
    :param value: Input value
    :return: factorial number
    """
    if value == 0 or value == 1:
        return 1

    return reduce(lambda n, n_1: n * n_1, range(1, (value + 1)))
