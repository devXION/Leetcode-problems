import pytest
class Solution:
    def thirdMax(self, nums: [int]) -> int:
        nums_set = set(nums)
        sorted_set = sorted(nums_set)
        return sorted_set[-3] if len(nums_set) >2 else sorted_set[-1]


        
@pytest.mark.parametrize('nums,output', [([3,2,1],1),([1,2],2),([2,2,3,1],1)])
def tester(nums,output):
    nums == output
