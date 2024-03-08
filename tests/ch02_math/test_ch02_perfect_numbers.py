import pytest

from ch02_math.ch02_perfect_number import calc_perfect_numbers


@pytest.mark.parametrize(
    "number, output",
    [
        (1000, [6, 28, 496]),
        (10000, [6, 28, 496, 8128]),
    ],
)
def test_perfect_numbers(number, output):
    result = calc_perfect_numbers(number)
    assert result == output
