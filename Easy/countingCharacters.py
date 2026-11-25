def counting(str):
    count  = 0

    for c in str:
        count+=1

    return count



string = input("Enter a string = ")
print(counting(string))