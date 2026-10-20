nums = [-5, -3, -2, -1, 1, 2]       # Expected: 3

def consecutive(list):
    if not list:
        return 0
    list = sorted(list)
    print(list)

    i = 0
    j = 1
    counter=0
    for _ in range(len(list)-1):
        difference = abs(list[i] - list[j])
        if difference == 1:
            counter+=1
            print(counter, "List item = ",list[i],list[j] )
        print("I am I = ", i, "I am J = ",j)
        i+=1
        j+=1
    return counter

print(consecutive(nums))