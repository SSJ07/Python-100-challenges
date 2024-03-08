"""
Prime numbers
"""
from typing import List


def is_prime_numbers(number: int) -> bool:
    """
    Check given number is prime or not.
    :param number: Number to check prime or not
    :return: True if number is prime. False otherwise
    """
    for val in range(2, (number // 2) + 1):
        if number % val == 0:
            return False
    return True


def calc_primes_up_to(max_value: int) -> List[int]:
    """
    Find all prime numbers up to given number
    :param max_value: Upper limit to find prime numbers
    :return: List of all prime numbers
    """
    if max_value < 2:
        return []
    prime_numbers: List[int] = [2]
    for val in range(3, max_value + 1):
        if is_prime_numbers(val):
            prime_numbers.append(val)
    return prime_numbers
