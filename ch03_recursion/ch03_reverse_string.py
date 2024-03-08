"""
Recursion function to reverse the string
"""


def reverse_string(text: str) -> str:
    """
    Reverse the string
    :param text: input string
    :return: reverse the string
    """
    rev_string = ""
    for i in range(len(text), 0, -1):
        rev_string += text[i]
    return rev_string


def reverse_string_optimized(text: str) -> str:
    if not isinstance(text, str):
        raise Exception("Input must be string")
    return text[::-1]


def reverse_string_with_recursion(text: str) -> str:
    if text == "":
        return text

    length = len(text) - 1
    if length == 0:
        return text[length]
    else:
        return text[length] + reverse_string_with_recursion(text[:length])
