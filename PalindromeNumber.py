def isPalindrome(
        x: int) -> bool:
    if (str(x) == str(x)[::-1]):
        return True
    else:
        return False
def tester():
    isPalindrome(121) == True
