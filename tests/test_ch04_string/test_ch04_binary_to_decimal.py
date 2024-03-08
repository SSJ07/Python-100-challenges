import pytest

from ch04_string.ch04_binary_to_decimal import convert_binary_to_decimal


@pytest.mark.parametrize("input_val, output", [
    (111, 7),
    (1111, 15),
    (1001, 9),
    (1011, 11),
    (10, 2),
    (110, 6),
])
def test_convert_binary_to_decimal(input_val, output):
    resp = convert_binary_to_decimal(input_val)
    assert resp == output
