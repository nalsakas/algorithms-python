class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

def traverse(root):
    current = root
    while current:
        print(current.val)
        current = current.next

def traverseRecursive(node):
    if node is None: return
    print(node.val)
    traverseRecursive(node.next)

def listValues(root):
    res = []
    current = root
    while current:
        res.append(current.val)
        current = current.next
    return res

def listValuesRecursive(node):
    if node is None:
        return []
    
    collect = listValuesRecursive(node.next)
    return [node.val, *collect]
    # single array
    # collect.insert(0, node.val)
    # return collect

def sumList(root):
    current = root
    total = 0
    while current:
        total += current.val
        current = current.next
    return total

def sumListRecursive(node):
    if node is None: return 0
    return sumListRecursive(node.next) + node.val

def listFind(root, target):
    current = root
    found = False
    while current:
        if current.val == target: found = True
        current = current.next
    return found

def listFindRecursive(node, target):
    if node is None: return False
    if node.val == target: return True

    return listFindRecursive(node.next, target)

def listGetValue(root, index):
    current = root
    while current:
        if index == 0:
            return current.val
        current = current.next
        index -= 1

def listGetValueRecursive(node, index):
    if node is None: return
    if index == 0: return node.val

    return listGetValueRecursive(node.next, index - 1) 

def reverseList(root):
    prev = None
    current = root
    
    while current:
        next = current.next

        current.next = prev

        prev = current
        current = next
    return prev

traverse(a)
traverseRecursive(a)
print(listValues(a))
print(listValuesRecursive(a))
print(listFind(a, 'a'))
print(listFind(a, 'e'))
print(listFindRecursive(a, "a"))
print(listFindRecursive(a, "e"))

a.val = 2
b.val = 8
c.val = 3
d.val = 7

print(sumList(a))
print(sumListRecursive(a))
print(listGetValue(a, 2))
print(listGetValue(a, 3))
print(listGetValue(a, 4))
print(listGetValueRecursive(a, 2))
print(listGetValueRecursive(a, 3))
print(listGetValueRecursive(a, 4))

print(listValues(a))
print(listValues(reverseList(a)))