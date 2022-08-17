def lengthOfLastWord(s: str) -> int:
    lastword = s.split()
    return len(lastword[-1])
