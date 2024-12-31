def mergeSort(a):
    if len(a) <= 1:
        return
    
    mid = len(a) // 2

    left = a[:mid]
    right = a[mid:]

    mergeSort(left)
    mergeSort(right)
    
    i = l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            a[i] = left[l]
            i += 1
            l += 1
        else:
            a[i] = right[r]
            i += 1
            r +=1 

    while l < len(left):
        a[i] = left[l]
        i += 1
        l += 1
    
    while r < len(right):
        a[i] = right[r]
        i += 1
        r += 1

if __name__ == "__main__":
    a1 = [2, 3, 1, 5, 4]
    a2 = [15, 14, 13, 10, 12, 11]
    
    mergeSort(a1)
    mergeSort(a2)
    print(a1)
    print(a2)