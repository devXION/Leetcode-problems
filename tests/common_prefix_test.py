import pytest

from leetcode.common_prefix import longestCommonPrefix


@pytest.mark.parametrize("xd,out", [
    (["flower", "flow", "flight"], 'fl'),
    (["dog", "racecar", "car"], '')
])
def test_longestCommonPrefix(xd, out):
    longestCommonPrefix(xd) == out
