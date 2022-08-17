import pytest

from leetcode.poweroftwo import is_power_of_two


@pytest.mark.parametrize('pow,state', [(1, True), (16, True), (3, False)])
def test_poweroftwo(pow, state):
    assert is_power_of_two(pow) == state
