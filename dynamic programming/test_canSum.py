from canSum import *

def test_canSum():
    assert canSum(7, [2, 3]) == True
    assert canSum(7, [5, 3, 4, 7]) == True
    assert canSum(7, [2, 4]) == False
    assert canSum(8, [2, 3, 5]) == True
    assert canSum(300, [7, 14]) == False