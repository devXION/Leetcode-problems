pytest.mark.parametrize('nums,output',[([2,7,11,15],[0,1]),([3,2,4],[1,2]),([3,3],[0,1])])
def tester(nums,output):
    nums == output