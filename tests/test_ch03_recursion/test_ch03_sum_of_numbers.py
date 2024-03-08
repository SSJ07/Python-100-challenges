import pytest

from ch03_recursion.ch03_sum_of_numbers import (
    calc_sum,
    calc_sum_with_reduce,
    sum_of_numbers,
    calc_sum_with_recursion,
    optimized_sum,
)


@pytest.mark.parametrize(
    "input_val,output",
    [
        (10, 55),
        (100, 5050),
        (30, 465),
        (1, 1),
    ],
)
def test_sum_of_numbers(input_val, output):
    nor_result = calc_sum_with_recursion(input_val)
    recursion_result = sum_of_numbers(input_val)
    reduce_result = calc_sum_with_reduce(input_val)
    lambda_result = calc_sum(input_val)
    formula_result = optimized_sum(input_val)

    assert nor_result == output
    assert recursion_result == output
    assert reduce_result == output
    assert reduce_result == output
    assert lambda_result == output
    assert formula_result == output
