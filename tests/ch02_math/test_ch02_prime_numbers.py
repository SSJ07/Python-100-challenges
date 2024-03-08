import pytest

from ch02_math.ch02_prime_numbers import calc_primes_up_to


@pytest.mark.parametrize(
    "max_value,output",
    [
        (15, [2, 3, 5, 7, 11, 13]),
        (25, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
        (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]),
        (1, []),
    ],
)
def test_prime_numbers(max_value, output):
    result = calc_primes_up_to(max_value)
    assert result == output
