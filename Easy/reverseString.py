string = "Your Name"


def reverser(string):
    result = ""

    for i in string:
        result = i + result


    return result


print(reverser(string))