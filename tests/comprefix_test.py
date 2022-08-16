@pytest.mark.parametrize("str,out", [(["flower","flow","flight"],'fl'),(["dog","racecar","car"],'')])
def tester(str,out):
    str == out