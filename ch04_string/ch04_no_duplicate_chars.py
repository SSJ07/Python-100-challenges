"""
Check no duplicates in given string
"""


def is_duplicate_in_text(text: str) -> bool:
    """
    Check if any duplicate char in given string

    Parameters
    ----------
    text: str
        Input string

    Returns
    -------
    bool
        False if duplicates in string, True otherwise
    """

    length = len(text)
    updated_text = text.lower()
    for index in range(length):
        if updated_text.count(text[index]) > 1:
            return False    
    return True

