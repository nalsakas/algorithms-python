def canConstruct(target, arr, s = ""):
    if s == target: return True
    if len(s) > len(target): return False

    for i in arr:
        if canConstruct(target, arr, s + i) == True:
            return True

    return False


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("abctdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))