meetings = [[0,30], [5,10], [15,20]]


def schedule(meetings):
    if not meetings:
        return meetings

    # Same Start Time
    room = 0
    start = []
    end = []
    max_room = 0

    for i in meetings:
        start.append(i[0])
        end.append(i[1])

    print("Start items = ",start)
    print("end items = ",end)

    
    start = sorted(i[0] for i in meetings)
    end = sorted(i[1] for i in meetings)

    print("Start items = ",start)
    print("end items = ",end)

    size = len(meetings)
    print("Size = ",size)

    i = 0
    j = 0
    while i < size and j < size:
        print(room)
        if (start[i] < end[j]):
            room+=1
            i += 1
            print(room)
        else:
            room -= 1
            j += 1

    max_room = max(max_room, room)
    return max_room     



print("total number or rooms",schedule(meetings))