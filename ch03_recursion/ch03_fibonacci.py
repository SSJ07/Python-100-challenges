"""
Fibonacci series
1 1 2 3 5 8 13
"""
from typing import List


def calc_fibonacci_series(val: int) -> List[int]:
    """
    Generate fibonacci series for given input.
    :param val: Input number
    :return: List of all fibonacci number
    """
    if val <= 1:
        return [1]

    a, b = 1, 0
    fibonacci_series: List[int] = []
    while val > 0:
        c = a + b
        fibonacci_series.append(c)
        a, b = b, c
        val -= 1
    return fibonacci_series
