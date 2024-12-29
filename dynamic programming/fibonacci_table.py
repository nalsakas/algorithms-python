def fibonacci(n):
    table = [0] * (n + 2)
    
    table[0] = 0
    table[1] = 1

    for i in range(n):
        table[i + 1] += table[i] 
        table[i + 2] += table[i]
    
    return table[n]

print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(50))