
def unidirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    print(hasPath(graph, nodeA, nodeB, visited= set()))

def buildGraph(edges):
    graph = {}

    for edge in edges:
        a,b = edge

        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph

def hasPath(graph, nodeA, nodeB, visited):
    if nodeA == nodeB: return True
    if nodeA in visited: return False
    visited.add(nodeA)

    for n in graph[nodeA]:
        if hasPath(graph, n, nodeB, visited) == True: return True

    return False

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

print(unidirectedPath(edges, 'i', 'n'))