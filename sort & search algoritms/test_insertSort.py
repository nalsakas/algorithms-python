from insertSort import *

def test_insertSort():
    a1 = [98, 34, 1, 87, 45, 54, 2, 3, 6, 11, 100]
    a2 = [9, 5, -1, 0, 56, 54, -10, -10, 9]
    
    insertSort(a1)
    insertSort(a2)

    assert a1 == [1, 2, 3, 6, 11, 34, 45, 54, 87, 98, 100]
    assert a2 == [-10, -10, -1, 0, 5, 9, 9, 54, 56]