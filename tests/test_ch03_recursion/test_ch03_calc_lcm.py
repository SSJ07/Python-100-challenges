import pytest

from ch03_recursion.ch03_calc_lcm import calc_lcm_iterative, calc_lcm_recursive


@pytest.mark.parametrize("num_1, num_2, output", [
    (2, 7, 14),
    (7, 14, 14),
    (42, 14, 42),
])
def test_calc_lcm(num_1, num_2, output):
    result = calc_lcm_iterative(num_1, num_2)
    higher_num = num_1 if num_1 > num_2 else num_2
    result_1 = calc_lcm_recursive(num_1, num_2, higher_num)
    assert result == output
    assert result_1 == output

