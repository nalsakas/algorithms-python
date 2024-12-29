def mergeSort(a: list[int], left: int, right: int):
    if right - left <= 1:
        return
    
    mid = (left + right) // 2

    mergeSort(a, left, mid)
    mergeSort(a, mid, right)

    merge(a, left, mid, right)

def merge(a, left, mid, right):
    sL = mid - left
    sR = right - mid

    aL = a[left : mid]
    aR = a[mid : right]
    
    i = j  = 0
    k = left

    while i < sL and j < sR:
        if aL[i] < aR[j]:
            a[k] = aL[i]
            i += 1
        else:
            a[k] = aR[j]
            j += 1 
        k += 1

    while i < sL:
        a[k] = aL[i]
        i += 1
        k += 1
    
    while j < sR:
        a[k] = aR[j]
        j += 1
        k += 1


def main():
    a1 = [2, 3, 1, 5, 4]
    a2 = [5, 4, 3 ,2, 1, 0]
    mergeSort(a2, 0, len(a2))
    print(a2)

if __name__ == "__main__":
    main()