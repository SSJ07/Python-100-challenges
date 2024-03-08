"""
Convert number to text
"""
from typing import Dict, List

NUMBER_MAP: Dict[int, str] = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "zero",
}


def number_as_text(number: int) -> str:
    """
    Convert given number into text.
    >>>number_as_text(10)
    ONE ZERO
    >>>number_as_text(201)
    TWO ZERO ONE
    :param number: Input number to convert into string
    :return: str: Converted string for given number
    """
    text_list: List[str] = []
    while number > 0:
        reminder = number % 10
        text_list.append(NUMBER_MAP.get(reminder).upper())
        number = number // 10

    text_list.reverse()
    return " ".join(text_list)
