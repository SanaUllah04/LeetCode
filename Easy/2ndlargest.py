list = [10, 5, 20, 8, 20, 4, 50, 90,80]



def secondLargest(list):
    value = 0
    temp = max(list)
    top = max(list)

    for i in list:
        diff = abs(top - i)
        if temp > diff & diff != 0:
            value = i
            temp = diff

    return value

print(secondLargest(list))