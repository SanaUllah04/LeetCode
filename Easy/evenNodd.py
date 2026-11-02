list = [1,2,3,4,5,6,7,8,9,10,11,12]

def niga(list):
    EvenCount = 0

    
    for i in range(len(list)):
        if list[i] % 2 == 0:
            EvenCount +=1


    return print("Total Number of Even = ", EvenCount, "Total Odds = ", len(list) - EvenCount)



niga(list)