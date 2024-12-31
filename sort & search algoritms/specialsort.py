def mySort(a):
    if len(a) <= 1:
        return a
    
    pivot = a[-1]

    left = [i for i in a if i < pivot]
    right = [i for i in a if i > pivot]

    return mySort(left) + [pivot] +  mySort(right)

    

if __name__ == "__main__":
    a = [3,2,1, 55, 32, 16, 78, 90, 54]
    print(mySort(a))