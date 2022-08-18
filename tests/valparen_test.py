import pytest

from leetcode.valparen import isValid


@pytest.mark.parametrize('symbol,state', [('()', True), ('(){}[]', True), ('(]', False)])
def test_valparen(symbol, state):
    assert isValid(symbol) == state
