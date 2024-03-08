"""
Check given number is binary or not
"""


def is_binary_number(binary_number: int) -> bool:
    """
    Validate given number is binary or not.

    Parameters
    ----------
    binary_number: int
        Input binary number

    Returns
    -------
    bool
        True if given number is binary, False otherwise

    """
    is_binary: bool = True
    while binary_number > 0:
        rem = binary_number % 10
        if rem > 1:
            is_binary = False
            break
        binary_number //= 10
    return is_binary


