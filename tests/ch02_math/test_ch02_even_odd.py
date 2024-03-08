"""Unit test for even or odd"""
import pytest

from ch02_math.ch02_even_odd import is_even, is_odd


@pytest.mark.parametrize(
    "number, expected",
    [
        (4, True),
        (2, True),
        (1, False),
        (7, False),
        (53, False),
    ],
)
def test_is_even(number, expected):
    result = is_even(number)
    assert result == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (4, False),
        (2, False),
        (1, True),
        (7, True),
        (53, True),
    ],
)
def test_is_odd(number, expected):
    result = is_odd(number)
    assert result == expected
