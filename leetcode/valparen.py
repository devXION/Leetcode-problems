def isValid(brackets: str) -> bool:
    if len(brackets) % 2 != 0:
        return False
    if brackets[0] in ')}]':
        return False
    opens = []
    for i in brackets:
        try:
            if i == '(':
                opens.append('(')
            elif i == '[':
                opens.append('[')
            elif i == '{':
                opens.append('{')

            elif i == ')':
                if opens.pop() != '(':
                    return False
            elif i == ']':
                if opens.pop() != '[':
                    return False
            elif i == '}':
                if opens.pop() != '{':
                    return False
        except IndexError:
            return False
    if len(opens) == 0:
        return True
    else:
        return False

