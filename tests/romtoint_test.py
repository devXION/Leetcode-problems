import pytest

from leetcode.romantoint import romanToInt


@pytest.mark.parametrize('ins,outs', [('III', 3), ('LVIII', 58), ('MCMXIV', 1914)])
def test_romantoint(ins, outs):
    assert romanToInt(ins) == outs
