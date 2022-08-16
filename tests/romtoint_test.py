@pytest.mark.parametrize('ins,outs',[('III', 3),('LVIII',58),('MCMXIV',1994)])
def tester(ins,outs):
    ins == outs