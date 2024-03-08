"""
Prime number pairs
"""
from typing import Dict

LIMIT: int = 50
PRIME_TYPES: Dict[str, int] = {"twin": 2, "cousin": 4, "sexy": 6}


def _is_prime(number: int) -> bool:
    """
    Check given number is prime or not.
    >>>_is_prime(5)
    True
    >>>_is_prime(8)
    False
    :param number: Number to check prime or not
    :return: True if number is prime. False otherwise
    """
    for i in range(2, (number // 2)):
        if number % i == 0:
            return False
    return True


def get_prime_number_pairs(prime_type: str) -> Dict[int, int]:
    """
    Get pairs of prime numbers
    :param prime_type: Type of prime pairs.
            Allowed values are: twin, cousin, and sexy
    :return: Dict[int, int]
    :raise: Exception
    """
    prime_pairs: Dict[int, int] = {}
    next_val = PRIME_TYPES.get(prime_type)
    if not next_val:
        raise Exception("Invalid prime type!")

    for num in range(3, LIMIT + 1):
        if _is_prime(num) and _is_prime(num + next_val):
            prime_pairs[num] = num + next_val
    return prime_pairs
