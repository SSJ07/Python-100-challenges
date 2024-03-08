"""
Max change Calculator

Problem statement:
    Suppose you have collection of coins or
    numbers of different values. Write a function
    calc_max_possible_change(values) that
    determines, for positive integers, what amounts can
    be seamlessly generated with it starting from the value 1.
    The maximum value should be returned as a result.
"""
from typing import List


def calc_max_possible_change(values: List[int]) -> int:
    """
    Find possible max change for given coins
    :param values: List of coins
    :return: Max possible change count
    """
    values.sort()
    max_possible_change: int = 0

    for current_value in values:
        if current_value > max_possible_change + 1:
            break
        max_possible_change += current_value

    return max_possible_change
