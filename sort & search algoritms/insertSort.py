def insertSort(a: list[int]):
    for i in range(1, len(a)):
        for j in range(i - 1, -1, -1):
            if a[j] > a[j + 1]  :
                a[j], a[j + 1] = a[j + 1], a[j]

if __name__ == '__main__':
    arr = [98, 34, 1, 87, 45, 54, 2, 3, 6, 11, 100]
    insertSort(arr)
    print(arr)