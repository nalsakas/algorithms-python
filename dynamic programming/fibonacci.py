def fibonacci(n, memo = None):
    if memo is None: memo = {}
    if n in memo: return memo[n]
    if n <= 2: return 1
    
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

if __name__ == '__main__':
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(5))
    print(fibonacci(50))