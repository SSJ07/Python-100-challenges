"""
Calculate Palindrome numbers
"""
from typing import Union


def is_palindrome(val: Union[int, str]) -> bool:
    """
    Check given input number is palindrome or not
    :param val: Input value
    :return: True if value is palindrome. False otherwise
    """

    length = len(val)
    if val == "":
        return False

    val = str(val) if isinstance(val, int) else val
    start = 0
    end = length - 1
    while start < end:
        if val[start] != val[end]:
            return False
        start += 1
        end -= 1
    return True


def is_palindrome_with_for_loop(val: str) -> bool:
    length = len(val)
    if val == "":
        return False
    for i in range(length // 2):
        if val[i] != val[length - 1 - i]:
            return False
    return True


def is_palindrome_optimized(val: str) -> bool:
    if val == "":
        return False
    return val == val[::-1]
