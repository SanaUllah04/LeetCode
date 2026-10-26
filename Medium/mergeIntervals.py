list =[[1,3],[2,6],[8,10],[15,18]]


def merging(list):
    start = []
    end = []
    final = []

 
    for i in range(len(list)):
        start.append(list[i][0])
        end.append(list[i][1])

    print("START = ",start, "END = ",end)

    first = 0
    last = 1
    j = 0
    merge = False

    for i in range(len(list)):
        print("AT J = ", j)

        if j == (len(list)-1):
            j = i
        else:
            j = i +1

        first = i
        last = j

        print("Iteration number = ", i)
        
        if (end[i] > start[j]) or (start[j] == end[i]):
            final.append([start[first], end[last]])
            merge = True

        else:
            if merge == True:
                i +=1 
                final.append([start[i], end[i]])
                merge = False
        


    return final

print(merging(list))