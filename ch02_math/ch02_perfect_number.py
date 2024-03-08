"""Perfect Number"""
from typing import List


def is_perfect_number(number: int) -> bool:
    """
    Check given number is perfect or not.
    >>>6 # 2 + 3 + 1 == 6
    True
    >>>7
    False
    :param number: Input number
    :return: True if given number is perfect. False otherwise
    """
    divisors: List[int] = []
    for n in range(1, (number // 2) + 1):
        if number % n == 0:
            divisors.append(n)
    return sum(divisors) == number


def calc_perfect_numbers(max_exclusive: int) -> List[int]:
    """
    Find all perfect numbers in given number range.
    >>>calc_perfect_numbers(1000)
    [6, 28, 496]
    :param max_exclusive: Max number limit
    :return: List of all perfect numbers
    """
    perfect_numbers: List[int] = []
    for number in range(2, max_exclusive):
        if is_perfect_number(number):
            perfect_numbers.append(number)
    return perfect_numbers
