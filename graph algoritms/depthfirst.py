graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def depthFirstPrint(graph, source):
    stack = [source]
    visited = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            print(current)
            for neighbor in graph[current]:
                stack.append(neighbor)

def depthFirstRecursivePrint(graph, source):
    print(source)

    for neighbor in graph[source]:
        depthFirstRecursivePrint(graph, neighbor)

def breadhFirstPrint(graph, source):
    queue = [source]
    visited = []

    while queue:
        current = queue.pop(0)
        if current not in visited:
            for neighbor in graph[current]:
                queue.append(neighbor)
            print(current)
            visited.append(current)


#depthFirstPrint(graph=graph, source='a')
#depthFirstRecursivePrint(graph=graph, source='a')
breadhFirstPrint(graph=graph, source='a')