@pytest.mark.parametrize('symbol,state',[('()', True),('(){}[]',True),('(]',False)])
def tester(symbol,state):
    symbol==state