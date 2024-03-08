
from ch02_math.ch02_computation_a import calc_combinations

EXPECTED_RESULT = [(3, 4, 5), (5, 12, 13), (7, 24, 25), (9, 40, 41), (11, 60, 61), (13, 84, 85)]


def test_computation_a():
    resp = calc_combinations()
    assert EXPECTED_RESULT == resp
