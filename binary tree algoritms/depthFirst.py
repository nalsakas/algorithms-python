from nodes import BinaryNode

def buildTree():
    a = BinaryNode('a')
    b = BinaryNode('b')
    c = BinaryNode('c')
    d = BinaryNode('d')
    e = BinaryNode('e')
    f = BinaryNode('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a

def buildIntTree():
    a = BinaryNode(3)
    b = BinaryNode(11)
    c = BinaryNode(4)
    d = BinaryNode(4)
    e = BinaryNode(2)
    f = BinaryNode(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a

def depthFirstValues(root):
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.val)
        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)


def depthFirstValues2(node):
    if node is None: return
    print(node.val)
    depthFirstValues2(node.right)
    depthFirstValues2(node.left)

def depthFirstValues3(node):
    if node is None: return []
    a = depthFirstValues3(node.right)
    b = depthFirstValues3(node.left)
    return [node.val, *a, *b]

def breadthFirstValues(root):
    queue = [root]
    val = []
    while queue:
        current = queue.pop(0)
        val.append(current.val)
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return val

def treeIncludes(node, target):
    if node is None: return False
    if node.val == target: return True

    leftVal = treeIncludes(node.left, target)
    rightVal =  treeIncludes(node.right, target)

    return leftVal or rightVal


def treeSum(node):
    if node is None: return 0

    leftSum = treeSum(node.left)
    rightSum = treeSum(node.right)

    return node.val + leftSum + rightSum

import math
def treeMin(node):
    if node is None: return math.inf

    leftVal = treeMin(node.left)
    rightVal = treeMin(node.right)

    return min(node.val, leftVal, rightVal)

def maxPathSum(node):
    if node is None: return -math.inf
    if node.left is None and node.right is None: return node.val
    
    leftSum = maxPathSum(node.left)
    rightSum = maxPathSum(node.right)

    return node.val + max(leftSum, rightSum)


#depthFirstValues(buildTree())
#depthFirstValues2(buildTree())
#print(depthFirstValues3(buildTree()))
#print(breadthFirstValues(buildTree()))
#print(treeIncludes(buildTree(), 'p'))
#print(treeSum(buildIntTree()))
#print(treeMin(buildIntTree()))
#print(maxPathSum(buildIntTree()))