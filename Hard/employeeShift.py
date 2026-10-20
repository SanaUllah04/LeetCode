shifts = [
    (9, 12),
    (10, 11),
    (11, 14),
    (12, 13),
    (13, 15)
]



def min_worker(list):
    if not list:
        return 0

    size = len(list)
    worker=0
    max_worker=0
    start = []
    end = []

    for i in list:
        start.append(i[0])
        end.append(i[1])

    start = sorted(i[0] for i in list)
    end = sorted(i[1] for i in list)

    print(start,end)

    i=0
    j=0

    while i < size and j < size:
        if start[i] < end[j]:
            worker+=1
            i+=1
            max_worker=max(max_worker, worker)
        else:
            worker-=1
            j+=1

    
    return max_worker

print(min_worker(shifts))