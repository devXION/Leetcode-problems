import pytest

nums=[]
def duo():
    for dup in nums:
        if nums.count(dup) < 2:
            nums.pop()
    print('List with duplicates is', nums)


duo()


@pytest.mark.parametrize('num,array', [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([1], 1)])
def tester(num, array):
    num == array
