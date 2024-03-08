import pytest

from ch02_math.ch02_basics import calc


@pytest.mark.parametrize("m, n, expected", [(6, 7, 0), (5, 5, 5)])
def test_calc(m, n, expected):
    result = calc(m, n)
    assert result == expected
