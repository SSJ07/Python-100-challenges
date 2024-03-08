import pytest

from ch03_recursion.ch03_fibonacci import calc_fibonacci_series


@pytest.mark.parametrize(
    "fib_num, output",
    [
        (5, [1, 1, 2, 3, 5]),
        (7, [1, 1, 2, 3, 5, 8, 13]),
        (8, [1, 1, 2, 3, 5, 8, 13, 21]),
        (1, [1]),
    ],
)
def test_fibonacci_series(fib_num, output):
    resp = calc_fibonacci_series(fib_num)
    assert resp == output
