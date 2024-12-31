def quickSort(a, left, right):
    if left >= right:
        return
    
    l = left
    r = right - 1
    p = right
    pivot = a[p]

    while l < r:
        while a[l] < pivot and l < right:
            l += 1
        
        while a[r] >= pivot and r > left:
            r -= 1

        if l < r:
            a[l], a[r] = a[r], a[l]

    if a[l] > pivot:
        a[p], a[l] = a[l], a[p]

    quickSort(a, left, l - 1)
    quickSort(a, l + 1, right)
    

if __name__ == "__main__":
    a = [3,2,1, 55, 32, 16, 78, 90, 54]
    quickSort(a, 0, len(a) - 1)
    print(a)