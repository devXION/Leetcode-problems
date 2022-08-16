@pytest.mark.parametrize('nums,output', [([3,2,1],1),([1,2],2),([2,2,3,1],1)])
def tester(nums,output):
    nums == output
