import pytest
def intToRoman(num: int) -> str:
    r = ''
    roman = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    for _, v in enumerate(roman):
        while num - roman[v] >= 0:
            r += v
            num -= roman[v]
    return r
@pytest.mark.parametrize('ins,outs',[('III', 3),('LVIII',58),('MCMXIV',1994)])
def tester(ins,outs):
    ins == outs
