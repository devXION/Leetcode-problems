import pytest
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]

@pytest.mark.parametrize('nums,output',[([2,7,11,15],[0,1]),([3,2,4],[1,2]),([3,3],[0,1])])
def tester(nums,output):
    nums == output
