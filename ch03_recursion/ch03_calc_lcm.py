"""
Find LCM
"""


def calc_lcm_iterative(num_1: int, num_2: int) -> int:
    """
    Find LCM using iterative way
    :param num_1: Input number 1
    :param num_2: Input number 2
    :return: LCM value
    """
    higher_num = num_2 if num_2 > num_1 else num_1
    for i in range(higher_num, (higher_num * 2) + 1):
        if i % num_1 == 0 and i % num_2 == 0:
            return i


def calc_lcm_recursive(num_1: int, num_2: int, modular: int) -> int:
    if modular % num_1 == 0 and modular % num_2 == 0:
        return modular
    calc_lcm_recursive(num_1, num_2, modular + 1)
