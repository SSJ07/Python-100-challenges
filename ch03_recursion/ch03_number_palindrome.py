"""
Number palindrome
"""


def is_number_palindrome(number: int) -> bool:
    """
    Validate number is palindrome or not.
    >>>is_number_palindrome(7)
    True
    >>>is_number_palindrome(171)
    True
    >>>is_number_palindrome(17)
    False
    :param number: Input number
    :return: True, If number is palindrome. False,otherwise.
    """
    if number < 10:
        return True

    temp = number
    total = 0
    while temp > 0:
        total = (total * 10) + (temp % 10)
        temp //= 10
    return total == number


def is_palindrome_with_recursive(number: int, num: int, total: int = 0) -> int:
    if number == 0:
        return total == num
    return is_palindrome_with_recursive(number//10, num, (total * 10) + (number % 10))
