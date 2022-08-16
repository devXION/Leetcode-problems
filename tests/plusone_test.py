@pytest.mark.parametrize('digit,array',[([1,2,3],[1,2,4]),([4,3,2,1],[4,3,2,2]),([9],[1,0])])
def tester(digit,array):
	digit == array
