mylist = [0,1,0,3,12]

def Mover(alist):
    i = 0
    size = len(alist)
    print("Total Size = ", size)

    for _ in range(size):
        if alist[i] == 0:
            del alist[i]
            alist.append(0)
        i+=1
        print("Step = ",i," List = ", alist)
        
    print("Total Size = ", size)
    return alist

print(Mover(mylist))