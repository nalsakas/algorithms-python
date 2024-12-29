import functools

@functools.cache
def gridTraveler(r, c):
    if r == 0 or c == 0:
        return 0
    if r == 1 and c == 1:
        return 1
    down = gridTraveler(r - 1, c)
    right = gridTraveler(r, c - 1)

    return down + right

print(gridTraveler(3, 2))