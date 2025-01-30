def howSum1(n, arr, memo = None):
    if memo is None: memo = {}
    if n in memo: return memo[n]

    if n < 0: return []
    if n == 0: return [[]]

    res = []
    for i in arr:
        collect = howSum1(n - i, arr, memo)
        res += list(map(lambda x: [i, *x], collect))
    memo[n] = res
    return memo[n]
    


def howSum2(n, arr):
    if n < 0: return []
    if n == 0: return [[]]
    
    res = []
    for i in arr:
        collect = howSum2(n - i, arr)
        res += list(map(lambda x: [i, *x], collect))

    return res


if __name__ == "__main__":
    print(howSum1(7, [2, 3]))
    #print(howSum1(7, [5, 3, 4, 7]))
    #print(howSum1(7, [2, 4]))
    #print(howSum1(8, [2, 3, 5]))
    #print(howSum1(300, [10, 7, 14]))

    #print(howSum2(7, [2, 3]))
    #print(howSum2(7, [5, 3, 4, 7]))
    #print(howSum2(7, [2, 4]))
    #print(howSum2(8, [2, 3, 5]))
    #print(howSum2(300, [10, 7, 14]))