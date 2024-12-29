from depthFirst import *

def test_depthFirstValues3():
    expected = ['a', 'c', 'f', 'b', 'e', 'd']
    assert depthFirstValues3(buildTree()) == expected

def test_treeSum():
    expected = 25
    assert treeSum(buildIntTree()) == expected 