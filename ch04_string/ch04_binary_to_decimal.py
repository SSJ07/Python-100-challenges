"""
Binary to Decimal conversion module
"""
import random


def convert_binary_to_decimal(binary_number: int) -> int:
    """
    Convert given binary number to decimal number

    Parameters
    ----------
    binary_number: int
        Binary number

    Returns
    -------
    int: Converted decimal number

    Examples
    --------
    >>> 101
    3
    >>> 111
    7

    """

    base_num: int = 2
    decimal_num: int = 0
    power: int = 0
    while binary_number > 0:
        rem = binary_number % 10
        decimal_num += (base_num**power) * rem
        power += 1
        binary_number //= 10

    return decimal_num
