def Reverse(name):
    if name == "":
        return name

    return Reverse(name[1:]) + name[0]


Name = input("Enter your name: ")
print(Reverse(Name))