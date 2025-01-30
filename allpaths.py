graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': ['f'],
    'f': []
}

def allPaths(graph, src, dst):
    
    if src == dst:
        return [[src]]
    
    collect = []
    
    for neighbor in graph[src]:
        paths = allPaths(graph, neighbor, dst)
        collect += list(map(lambda x: [src, *x], paths))
    
    return collect


print(allPaths(graph=graph, src='a', dst='f'))
print(allPaths(graph=graph, src='f', dst='a'))