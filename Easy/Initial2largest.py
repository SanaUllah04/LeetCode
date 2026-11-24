list = [4,8,1,0,2,3,5,7,6,9]

def Large(myList):
    largest = 0
    secondLargest = 0

    for i in range(len(myList)):
        if largest < i:
            largest = i

    for j in range(len(myList)):
        if secondLargest < j and j != largest:
            secondLargest = j

    return largest, secondLargest

print(Large(list))