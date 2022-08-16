import pytest

nums=[]
def duo():
    for dup in nums:
        if nums.count(dup) < 2:
            nums.pop()
    print('List with duplicates is', nums)


duo()



