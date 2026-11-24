list = [4,8,1,0,2,3,5,7,6,9]

def Large(myList):
    largest = max(myList)
    myList.remove(max(myList))
    secondLargest = max(myList)

    return largest, secondLargest




print(Large(list))