import pytest

from ch04_string.ch04_no_duplicate_chars import is_duplicate_in_text


@pytest.mark.parametrize("text, output",[
    ("Otto", False),
    ("Adrian", False),
    ("Micha", True),
])
def test_no_duplicates(text, output):
    resp = is_duplicate_in_text(text)
    assert resp == output
