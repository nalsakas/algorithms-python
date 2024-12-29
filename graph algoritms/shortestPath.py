edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

def edgesToGraph(edges):
    graph = {}

    for edge in edges:
        a, b = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    
    return graph

def shortestPath(edges, src, dst):
    graph = edgesToGraph(edges)
    queue = [[src, 0]]
    visited = set()

    while queue:
        current, dist = queue.pop(0)
        if current == dst: return dist
        if current in visited: continue
        visited.add(current)

        for n in graph[current]:
            queue.append([n, dist + 1])
    
    return -1
    
print(shortestPath(edges, 'w', 'y'))