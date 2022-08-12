@pytest.mark.parametrize("number,listing", [(3, ["1", "2", "Fizz"]), (5, ["1", "2", "Fizz", "4", "Buzz"]), (
15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])])
def tester(number, listing):
    assert fizzBuzz(number) == listing
