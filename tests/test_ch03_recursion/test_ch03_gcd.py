import pytest

from ch03_recursion.ch03_calc_gcd import calc_gcd, calc_gcd_iterative


@pytest.mark.parametrize("num_1, num_2, output", [
    (42, 7, 7),
    (42, 28, 14),
    (42, 14, 14),
])
def test_calc_gcd(num_1, num_2, output):
    resp = calc_gcd(num_1, num_2, num_2)
    resp_1 = calc_gcd_iterative(num_1, num_2)
    assert resp == output
