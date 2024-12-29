import math

graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2] 
}

def largestComponent(graph):
    largest = -math.inf
    count = 0
    visited = set()

    for node in graph:
        count = explore(graph, node, visited)
        if count > largest: largest = count

    return largest

def explore(graph, node, visited):
    if node in visited: return 0
    visited.add(node)
    sum = 1

    for i in graph[node]:
        sum += explore(graph, i, visited) 

    return sum

print(largestComponent(graph))