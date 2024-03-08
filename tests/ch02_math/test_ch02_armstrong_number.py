import pytest

from ch02_math.ch02_armstrong_number import is_armstrong_number, calc_armstrong_number


@pytest.mark.parametrize(
    "number,output",
    [
        (123, False),
        (1233, False),
        (153, True),
        (371, True),
    ],
)
def test_armstrong_number(number, output):
    resp = is_armstrong_number(number)
    assert resp == output


@pytest.mark.parametrize(
    "number,output",
    [
        (100, []),
        (200, [153]),
        (500, [153, 370, 371, 407]),
    ],
)
def test_armstrong_numbers(number, output):
    resp = calc_armstrong_number(number)
    assert resp == output
