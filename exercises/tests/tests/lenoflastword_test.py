@pytest.mark.parametrize("word, number", [("joyboy", 6)])
def tester(word,number):
    assert lengthOfLastWord(word) == number