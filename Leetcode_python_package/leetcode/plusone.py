import pytest
class Solution(object):
		def plusOne(self, digits):
			s=""
			for i in digits:
				s +=str(i)
			return list(str(int(s) + 1))
