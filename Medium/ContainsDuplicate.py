mylist = [1,2,3,1]

def ContainsDuplicates(alist):

    print("Given LIST = ", mylist, type(alist))

    for i in range(len(alist)):
        if alist.count(alist[i]) >= 2:
            print(alist[i], " is a Duplicate")
            return True

        return False




print(ContainsDuplicates(mylist))