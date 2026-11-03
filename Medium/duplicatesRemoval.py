malis = [1,1,2,2,3]

def Remover(malis):
    first = 0
    second = 1
    trasporter = 0

    for _ in range(len(malis)):
        for _ in range(len(malis)):
            if(malis[first] == malis[second]):
                del malis[second]
                second+=1
                first+=1

            if second == len(malis):
                second = 0


    return malis

                

print(type(malis))
print(malis)
malis.sort()
print(malis)
print(Remover(malis))