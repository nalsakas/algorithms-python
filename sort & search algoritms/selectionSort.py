def selectionSort(a: list[int]):
    for i in range(len(a)):
        smallest = i
        for j in range(i + 1, len(a)):
            if a[j] < a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]

def main():
    a1 = [2, 3, 1, 5, 4]
    a2 = [5, 4, 3 ,2, 1, 0]
    selectionSort(a2)
    print(a2)

if __name__ == "__main__":
    main()

