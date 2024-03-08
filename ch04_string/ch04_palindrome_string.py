"""
Check given string is palindrome or not
"""


def is_text_palindrome(string: str) -> bool:
    """
    Check given text is palindrome or not

    Parameters
    ----------
    string: str
        Input text value

    Returns
    -------
    bool
        True if string is palindrome, False otherwise

    Examples
    --------
    >>> is_text_palindrome("AbBa")
    True
    >>> is_text_palindrome("CDEAHD")
    False
    """
    is_palindrome: bool = True
    length = len(string)
    for index in range(length//2):
        if string[index].lower() != string[length-1-index].lower():
            is_palindrome = False
            break
    return is_palindrome
