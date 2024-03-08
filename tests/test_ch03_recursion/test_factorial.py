import pytest

from ch03_recursion.ch03_factorial import (
    calc_factorial_with_normal_loop,
    calc_factorial_with_recursion,
    calc_factorial_with_reduce,
    factorial,
)


@pytest.mark.parametrize(
    "input_val,output",
    [
        (5, 120),
        (6, 720),
        (0, 1),
        (1, 1),
    ],
)
def test_factorial(input_val, output):
    nor_result = calc_factorial_with_normal_loop(input_val)
    recursion_result = calc_factorial_with_recursion(input_val)
    reduce_result = calc_factorial_with_reduce(input_val)
    lambda_result = factorial(input_val)

    assert nor_result == output
    assert recursion_result == output
    assert reduce_result == output
    assert reduce_result == output
    assert lambda_result == output
