import pytest

from leetcode.fizzbuzz import fizzBuzz


@pytest.mark.parametrize("number,output", [(3, ["1", "2", "Fizz"]), (5, ["1", "2", "Fizz", "4", "Buzz"])])
def test_fizzbuzz(number, output):
    assert fizzBuzz(number) == output
