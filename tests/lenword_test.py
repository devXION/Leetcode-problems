@pytest.mark.parametrize("word,lenght", [("Hello World", 5),("joyboy", 6)])
def tester(word,lenght):
    lengthOfLastWord(word) == lenght