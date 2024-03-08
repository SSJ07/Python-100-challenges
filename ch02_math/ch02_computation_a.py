"""
Program to find combinations of below formula:
a2 + b2 = c2
"""
from typing import List, Tuple


def calc_combinations() -> List[Tuple[int, int, int]]:
    """
    Find all combinations of below formula:
    a2 + b2 = c2
    >>> calc_combinations()
    [(3, 4, 5)]
    :return: List of all numbers that satisfies above condition
    """
    squares: List[Tuple[int, int, int]] = []
    for a in range(1, 101):
        a_square = a * a
        for b in range(1, 101):
            c = b + 1
            b_square = b * b
            c_square = c * c
            if (a_square + b_square) == c_square:
                squares.append((a, b, c))
    return squares
