from bubbleSort import *

def test_bubleSort():
    a1 = [2, 3, 1, 5, 4]
    a2 = [5, 4, 2 ,3, 1, 0]

    bubbleSort(a1)
    bubbleSort(a2)
    
    assert a1 == [1, 2, 3, 4, 5]
    assert a2 == [0, 1, 2, 3, 4, 5]