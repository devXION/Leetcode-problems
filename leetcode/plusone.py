import pytest
class Solution(object):
		def plusOne(self, digits):
			s=""
			for i in digits:
				s +=str(i)
			return list(str(int(s) + 1))
@pytest.mark.parametrize('digit,array',[([1,2,3],[1,2,4]),([4,3,2,1],[4,3,2,2]),([9],[1,0])])
def tester(digit,array):
	digit == array
