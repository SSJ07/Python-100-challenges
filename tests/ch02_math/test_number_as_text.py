import pytest

from ch02_math.ch02_number_as_text import number_as_text


@pytest.mark.parametrize(
    "number, expected",
    [
        (7, "SEVEN"),
        (42, "FOUR TWO"),
        (24680, "TWO FOUR SIX EIGHT ZERO"),
        (13579, "ONE THREE FIVE SEVEN NINE"),
    ],
)
def test_number_as_text(number, expected):
    result = number_as_text(number)
    assert result == expected
