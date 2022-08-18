import pytest

from leetcode.majority import majorityElement


@pytest.mark.parametrize("list, value", [([3, 2, 3], 3), ([4, 2, 4], 4)])
def test_majority(list, value):
    assert majorityElement(list) == value
