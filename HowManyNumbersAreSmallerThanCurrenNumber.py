def smallerNumbersThanCurrent(nums):
    d = {}
    for i, n in enumerate(sorted(nums)):
        if n not in d: d[n] = i
    return [d[i] for i in nums]


def tester():
    smallerNumbersThanCurrent([6,5,4,8]) == [2,1,0,3]
