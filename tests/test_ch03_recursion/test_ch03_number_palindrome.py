import pytest

from ch03_recursion.ch03_number_palindrome import (
    is_number_palindrome,
    is_palindrome_with_recursive,
)


@pytest.mark.parametrize(
    "number, output", [(7, True), (13, False), (171, True), (47742, False)]
)
def test_is_number_palindrome(number, output):
    resp = is_palindrome_with_recursive(number, number)
    assert resp == output
