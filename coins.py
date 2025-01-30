coins = {
    #'0.1': 5,
    #'0.2': 5,
    #'0.5': 5,
    '1': 10,
    '2': 10,
    '5': 10,
    '10': 2,
    '50': 1,
    '100': 1
}

def allPaths(coins, amount):
    
    if amount == 0:
        return [[]]
    elif amount < 0:
        return []
    
    collect = []
    for coin in coins:
        dif = amount - int(coin)
        paths = allPaths(coins, dif)
        collect += list(map(lambda x: [coin, *x], paths))
    
    return collect


#print(allPaths(coins=coins, amount=1))
print(allPaths(coins=coins, amount=10))