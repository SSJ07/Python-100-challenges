"""
Problem: Count as well as sum up the natural numbers divisible by 2 or 7
"""
from typing import Tuple


def calc_sum_and_count_nums_divisible_by_2_or_7(num: int) -> Tuple[int, int]:
    """
    Sum up and count all natural numbers divisible by 2 or 7
    :param num: Numbers within given number
    :return: Tuple[int, int]
    """
    nums = []
    for num in range(2, num + 1):
        if (num % 2 == 0) or (num % 7 == 0):
            nums.append(num)
    return len(nums), sum(nums)
