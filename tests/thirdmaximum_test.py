import pytest

from leetcode.thirdmaximum import thirdMax


@pytest.mark.parametrize('nums,output', [([3, 2, 1], 1), ([1, 2], 2), ([2, 2, 3, 1], 1)])
def test_thirdmax(nums, output):
    assert thirdMax(nums) == output
