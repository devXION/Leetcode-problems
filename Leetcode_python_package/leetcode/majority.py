from statistics import mode
import pytest


def majorityElement(nums: list[int]) -> int:
    return mode(nums)
