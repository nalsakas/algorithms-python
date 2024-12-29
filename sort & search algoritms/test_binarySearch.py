from binarySearch import *

def test_binarySearch():
    arr = [1,3,4,5,6,7,8,45,67,77,0,99]
    
    assert binarySearch(arr, 0, len(arr), 77) == 9
    assert binarySearch(arr, 0, len(arr), 99) == 11
    assert binarySearch(arr, 0, len(arr), 101) == -1