import pytest
def isPalindrome(
        x: int) -> bool:
    if (str(x) == str(x)[::-1]):
        return True
    else:
        return False
@pytest.mark.parametrize('number,condition',[(121,True),(-121,False),(10,False)])
def tester(number,condition):
    number == condition

