from gridTraveler import *

def test_gridTraverler():
    assert gridTraveler(1, 1) == 1
    assert gridTraveler(2, 3) == 3
    assert gridTraveler(3, 2) == 3
    assert gridTraveler(3, 3) == 6
    assert gridTraveler(18, 18) == 2333606220