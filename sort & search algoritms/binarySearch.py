def binarySearch(arr, start, end, target):
    if start >= end: return -1

    mid = (end + start) // 2
    if arr[mid] == target: 
        return mid
    
    right = binarySearch(arr, mid + 1, end, target)
    left = binarySearch(arr, start, mid - 1, target)

    if right == -1 and left == -1:
        return -1
    elif right == -1 or left == -1:
        return max(right, left)
    else:
        return min(right. left)
    
if __name__ == '__main__':
    arr = [1,3,4,5,6,7,8,45,67,77,0,99]
    print(binarySearch(arr, 0, len(arr), 101)) # -1