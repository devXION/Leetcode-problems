class Solution:
    def smallerNumbersThanCurrent(self, nums):
        d = {}
        for i,n in enumerate(sorted(nums)):
            if n not in d: d[n]=i
        return [d[i] for i in nums]
assert  nums == [8,1,2,2,3]
assert  nums == [6,5,4,8]
assert  nums == [7,7,7,7]
