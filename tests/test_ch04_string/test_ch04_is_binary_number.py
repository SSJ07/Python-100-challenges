import pytest

from ch04_string.ch04_is_binary_number import is_binary_number


@pytest.mark.parametrize("input_number, expected", [
    (1010101, True),
    (10334, False),
    (10000, True),
    (234234, False),
])
def test_is_binary_number(input_number, expected):
    resp = is_binary_number(input_number)
    assert resp == expected
