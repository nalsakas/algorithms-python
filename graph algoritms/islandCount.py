island_grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'L'],
    ['L', 'L', 'W', 'L', 'W']
]

def islandCount(grid):
    count = 0
    rowLength = len(island_grid)
    columnLength = len(island_grid[0])
    visited = set()
    largest = 0

    for r in range(rowLength):
        for c in range(columnLength):
            size = explore(grid, r, c, visited)
            if size != 0: count += 1
            if size > largest: largest = size

    return count, largest

def explore(grid, r, c, visited):
    if r < 0 or r > len(grid) - 1: return 0
    if c < 0 or c > len(grid[0]) - 1: return 0

    node = grid[r][c]
    if node == 'W': return 0
    if f"${r}${c}" in visited: return 0
    visited.add(f"${r}${c}")
    sum = 1

    sum += explore(grid, r + 1, c, visited)
    sum += explore(grid, r, c + 1, visited)
    sum += explore(grid, r - 1, c, visited)
    sum += explore(grid, r, c - 1, visited)

    return sum


print(islandCount(island_grid))