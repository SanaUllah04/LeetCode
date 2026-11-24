
def Reverse(name):
    reversedName = ""

    for char in (name):
        reversedName =  char + reversedName

    
    return reversedName



Name = input("Enter a String = ")
print(Reverse(Name))