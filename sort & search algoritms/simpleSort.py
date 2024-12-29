def simpleSort(a: list[int]):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a [i] > a[j]:
                a[i], a[j] = a[j], a[i]

def main():
    a1 = [2, 3, 1, 5, 4]
    a2 = [5, 4, 2 ,3, 1, 0]
    simpleSort(a2)
    print(a2)

if __name__ == "__main__":
    main()