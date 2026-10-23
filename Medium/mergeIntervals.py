list = [[1,4],[4,5]]


def merging(list):
    start = []
    end = []

    print(type(list))
    for i in range(len(list)):
        print("List Item = ",list[i], "AT I = ", i)
        start.append(list[i][0])
        end.append(list[i][1])

    print("START = ",start, "END = ",end)

    for i in range(len(list)-1):
        diff = abs(start[i+1] - end[i])

        if (start[i+1] > end[i]) and (diff == 1):
            print("Start I+1 = ", start[i+1])
            print("niga")


print(merging(list))