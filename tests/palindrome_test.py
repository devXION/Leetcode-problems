import pytest

from leetcode.palindrome import isPalindrome


@pytest.mark.parametrize('number,condition', [(121, True), (-121, False), (10, False)])
def test_palindromenumber(number, condition):
    assert isPalindrome(number) == condition
