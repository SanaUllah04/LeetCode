palindrome = "A man a plan a canal Panama"

def PalindromeConfirm(string):
    confirm = False
    first = 0
    last = len(string)-1
    half = len(string)//2
    print(type(half))

    print("Value of First = ", first, "Value of LAST = ", last)
    print("Total Iterations = ",half)

    for _ in range(half):
        print("Value of First = ", first, "Value of LAST = ", last)

        if (string[first] != string[last]):
            confirm = False
            return confirm

        else:
            confirm = True
            first +=1
            last -= 1

    return confirm 
        

palindrome = palindrome.lower()
palindrome = palindrome.replace(" ", "")

print(palindrome)

print(PalindromeConfirm(palindrome))