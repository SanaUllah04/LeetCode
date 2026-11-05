meetings = [[0,30],[5,10],[15,20]]


def numberOfRooms(alist):
    start = []
    end = []
    room = 0

    for i in range(len(alist)):
        start.append(alist[i][0])
        end.append(alist[i][1])

    print("Start = ", start, " END = ", end)

    start.sort()
    end.sort()
    print("Sorted --- Start = ", start, " END = ", end)

    i = 0
    j = 0
    size = len(alist)

    while i<size and j<size:
        if(start[i] < end[j]):
            room +=1
            i+=1
        else:
            room-=1
            j+=1

    return room


print(numberOfRooms(meetings))