import pytest

from leetcode.smallerthancurrent import smallerNumbersThanCurrent


@pytest.mark.parametrize('nums,out', [([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]), ([6, 5, 4, 8], [2, 1, 0, 3]),
                                      ([7, 7, 7, 7], [0, 0, 0, 0])])
def test_smallerthancurrent(nums, out):
    assert smallerNumbersThanCurrent(nums) == out
