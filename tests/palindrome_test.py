@pytest.mark.parametrize('number,condition',[(121,True),(-121,False),(10,False)])
def tester(number,condition):
    number == condition
