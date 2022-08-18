def thirdMax(nums: [int]) -> int:
    nums_set = set(nums)
    sorted_set = sorted(nums_set)
    return sorted_set[-3] if len(nums_set) > 2 else sorted_set[-1]
