def canSum (n, arr, memo = None):
    if memo is None: memo = {}
    if n in memo: return memo[n]
    if n < 0: return False
    if n == 0: return True

    collect = False
    for i in arr:
        collect |= canSum(n - i, arr, memo)
    
    memo[n] = collect
    return memo[n]

if __name__ == "__main__":
    print(canSum(7, [2, 3]))
    print(canSum(7, [5, 3, 4, 7]))
    print(canSum(7, [2, 4]))
    print(canSum(8, [2, 3, 5]))
    print(canSum(300, [7, 14]))