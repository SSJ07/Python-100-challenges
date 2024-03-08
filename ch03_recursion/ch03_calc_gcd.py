"""
Find GCD using recursion
"""


def calc_gcd(num_1: int, num_2: int, modular: int) -> int:
    """
    Find GCD for given numbers.
    :param modular: moduler num / GCD num
    :param num_1: First number
    :param num_2: Second Number
    :return: GCD for given numbers
    """
    if modular < (num_2//2):
        return 1
    if (num_2 % modular == 0) and (num_1 % modular == 0):
        return modular
    return calc_gcd(num_1, num_2, modular - 1)


def calc_gcd_iterative(num_1: int, num_2: int) -> int:
    """
    Find GCD for given numbers
    :param num_1: First number
    :param num_2: Second number
    :return: GCD number
    """
    lowest_number = num_2 if num_2 < num_1 else num_1
    for i in range(lowest_number, 1, -1):
        if num_2 % i == 0 and num_1 % i == 0:
            return i
