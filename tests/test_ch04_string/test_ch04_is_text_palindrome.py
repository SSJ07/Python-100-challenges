import pytest

from ch04_string.ch04_palindrome_string import is_text_palindrome


@pytest.mark.parametrize("text, expected_output", [
    ("Otto", True),
    ("ABCEX", False),
    ("A", True),
    ("ABCEcba", True),
])
def test_is_text_palindrome(text, expected_output):
    resp = is_text_palindrome(text)
    assert resp == expected_output
