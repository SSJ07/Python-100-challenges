"""Armstrong number"""
from typing import List


def is_armstrong_number(num: int) -> bool:
    """
    Checks given number is armstrong or not.
    :param num: Number to verify it's armstrong or not
    :return: True if satisfies condition. False otherwise
    """
    temp = num
    total = 0
    while temp > 0:
        total += (temp % 10) ** 3
        temp //= 10
    return num == total


def calc_armstrong_number(number: int) -> List[int]:
    """
    Find all armstrong numbers in given limit
    :param number: Range to find armstrong numbers
    :return: List of all armstrong numbers in given range
    """

    if number < 0:
        raise Exception("Number should be positive")

    nums: List[int] = [n for n in range(10, number) if is_armstrong_number(n)]
    return nums
