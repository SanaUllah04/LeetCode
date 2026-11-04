mylist = [0,0,0,2,4,0,0,0,0,0,0,0,1,3,12]

def Mover(alist):

    size = len(alist)
    print("Total Size = ", size)
    total_Zeros = alist.count(0)
    i = 0

    for _ in range(len(alist)-2):
        if alist[i] == 0:
            del alist[i]
        if alist[i] != 0:
            i+=1

    for i in range(total_Zeros):
        alist.append(0)

    return alist

print("MY LIST = ",mylist)
print(Mover(mylist))