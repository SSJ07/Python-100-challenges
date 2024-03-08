"""
Check sum
"""
MOD_VALUE: int = 10


def calc_checksum(digits: str) -> int:
    """
    Calculate checksum of given digits
    :param digits: string formatted digits
    :return: checksum of given digits
    """
    checksum: int = 0
    for index, val in enumerate(digits, start=1):
        checksum += (index * int(val))
    return checksum % MOD_VALUE
