import pytest

from leetcode.lenoflastword import lengthOfLastWord


@pytest.mark.parametrize("word,lenght", [("Hello World", 5), ("joyboy", 6)])
def test_lenoflastword(word, lenght):
    assert lengthOfLastWord(word) == lenght
