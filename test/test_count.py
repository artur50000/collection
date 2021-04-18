from count import count
import pytest

@pytest.mark.parametrize("test_input,expected", [("asssdffx!!", 3), ("aaasssddffxx!!", 0), ("asdfx!", 6)])
def test_count(test_input,expected):
    assert count.unique_letters(test_input) == expected
