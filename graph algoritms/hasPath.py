graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def hasPath(graph, src, dst):
    
    if src == dst:
        return True

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst) == True:
            return True

    return False

print(hasPath(graph=graph, src='a', dst='f'))
print(hasPath(graph=graph, src='f', dst='a'))