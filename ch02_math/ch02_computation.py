"""
Write a program to compute all combinations of the values a,b,c and d
Each starts from 1 and less than UPPER_LIMIT
"""
from typing import List, Tuple, Any


def calc_computations() -> list[tuple[int, int, int, int]]:
    """
    combinations of values a, b, c, and d.
    a2 + b2 = c2 + d2
    :return: List of tuple
    """
    LOWER_LIMIT: int = 1
    UPPER_LIMIT: int = 100

    all_combinations: List[Tuple[int, int, int, int]] = []
    for i in range(LOWER_LIMIT, UPPER_LIMIT):
        i_square = i ** 2
        for b in range(LOWER_LIMIT, UPPER_LIMIT):
            b_square = b ** 2
            for c in range(LOWER_LIMIT, UPPER_LIMIT):
                d = c + 1
                c_square, d_square = c ** 2, d**2
                if b != c and (i_square + b_square) == (c_square + d_square):
                    all_combinations.append((i, b, c, d))
    return all_combinations


if __name__ == '__main__':
    resp = calc_computations()
    print(resp)
