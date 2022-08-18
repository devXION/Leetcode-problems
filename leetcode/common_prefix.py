
def longestCommonPrefix( strs: list[str]) -> str:
    if len(strs) == 0:
        return ""
    s = strs[0]
    for i in range(1, len(strs)):
        while strs[i][0:len(s)] != s:
            s = s[0:len(s) - 1]
            if len(s) == 0:
                return ""
    return s

