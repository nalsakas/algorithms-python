def allConstruct(target:str, arr, memo = None):
    if memo is None: memo = {}
    if target in memo: return memo[target]

    if target == "": return [[]]

    collect = []
    for i in arr:
        if target.find(i) == 0:
            subtarget = target[len(i):]
            res = allConstruct(subtarget, arr, memo)
            collect += list(map(lambda x: [i, *x], res))
        
    memo[target] = collect
    return memo[target]


print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "ef"]))
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstruct("purple", ["purp", "le", "p", "urple"]))
print(allConstruct("0123456789", ["0", "1", "2", "3", "4","5", "6", "7", "8", "9", "789", "0123"]))