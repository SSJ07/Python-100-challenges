import pytest

from ch02_math.ch02_checksum import calc_checksum


@pytest.mark.parametrize("digits, output", [
    ("11111", 5),
    ("87654321", 0),
])
def test_calc_checksum(digits, output):
    result = calc_checksum(digits)
    assert result == output
