from statistics import mode
import pytest


def majorityElement(nums: list[int]) -> int:
    return mode(nums)
@pytest.mark.parametrize("list, value", [([3,2,3], 3),([4,2,4], 4)])
def tester(list, value):
    majorityElement(list) == value