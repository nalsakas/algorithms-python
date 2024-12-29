def allConstruct(target, arr, s = ""):
    if s == target: return [[]]
    if len(s) > len(target): return []

    collect = []
    for i in arr:
        res = allConstruct(target, arr, s + i)
        collect += list(map(lambda x: [i, *x], res))

    return collect 


print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(allConstruct("abctdef", ["ab", "abc", "cd", "def", "abcd"]))
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstruct("purple", ["purp", "le", "p", "urple"]))
print(allConstruct("0123456789", ["01", "22346", "789", "0123", "456", "789"]))