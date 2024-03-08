import pytest

from ch02_math.ch02_sum_and_count import calc_sum_and_count_nums_divisible_by_2_or_7


@pytest.mark.parametrize(
    "max_number, count, summ", [(3, 1, 2), (8, 4, 19), (15, 8, 63)]
)
def test_sum_and_count_divisible_by_2_or_7(max_number, count, summ):
    count, summ = calc_sum_and_count_nums_divisible_by_2_or_7(max_number)
