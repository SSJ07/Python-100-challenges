import pytest

from ch03_recursion.ch03_palindrome import (
    is_palindrome,
    is_palindrome_optimized,
)

fake_string = "".join([chr(x) for x in range(65, 91) for i in range(100)])
fake_string = f"{fake_string}{fake_string[::-1]}"


@pytest.mark.parametrize(
    "input_val, output",
    [
        ("A", True),
        ("ABCDE", False),
        ("", False),
        ("ABCDCBA", True),
        (fake_string, True),
    ],
)
def test_is_palindrome(input_val, output):
    resp = is_palindrome(input_val)
    resp1 = is_palindrome_optimized(input_val)
    assert resp == output
    assert resp1 == output
