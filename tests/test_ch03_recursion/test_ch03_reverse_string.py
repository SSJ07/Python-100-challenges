import pytest

from ch03_recursion.ch03_reverse_string import reverse_string_with_recursion


@pytest.mark.parametrize("string, output",[
    ("Hello", "olleH"),
    ("Hello Python", "nohtyP olleH"),
    ("", ""),
])
def test_reverse_string(string, output):
    result = reverse_string_with_recursion(string)
    assert output == result

