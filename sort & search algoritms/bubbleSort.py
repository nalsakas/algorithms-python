def bubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
               a[j], a[j + 1] = a[j + 1], a[j]


if __name__ == "__main__":
    a1 = [2, 3, 1, 5, 4]
    a2 = [5, 4, 2 ,3, 1, 0]
    bubbleSort(a1)
    bubbleSort(a2)
    print(a1)
    print(a2)