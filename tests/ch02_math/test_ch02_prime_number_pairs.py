import pytest

from ch02_math.ch02_prime_number_pairs import get_prime_number_pairs


@pytest.mark.parametrize(
    "prime_type,output",
    [
        ("twin", {3: 5, 5: 7, 11: 13, 17: 19, 29: 31, 41: 43}),
        ("cousin", {3: 7, 7: 11, 13: 17, 19: 23, 37: 41, 43: 47}),
        (
            "sexy",
            {
                5: 11,
                7: 13,
                11: 17,
                13: 19,
                17: 23,
                23: 29,
                31: 37,
                37: 43,
                41: 47,
                47: 53,
            },
        ),
        ("dummy", "Invalid prime type!"),
    ],
)
def test_get_prime_number_pairs(prime_type, output):
    if prime_type == "dummy":
        with pytest.raises(Exception):
            get_prime_number_pairs(prime_type)
    else:
        result = get_prime_number_pairs(prime_type)
        assert result == output
