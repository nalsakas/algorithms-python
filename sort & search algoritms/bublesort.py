s = list(map(int, list(input().strip())))
n = len(s)
k = 0

for i in range(n):
    for  j in range(n - 1):
        if  s[j] > s[j + 1]:
            s[j], s[j + 1] = s[j + 1], s[j]
            k = k + 1

for i in s:
    print(str(i), sep="", end="")

print("\n", end="")