requests = [(1,"A"), (2,"A"), (3,"B"), (4,"A"), (10,"B"), (11,"B"), (12,"B")]
K = 3
W = 5

def spammyUsers(list):
    if not requests:
        return 0

    spammers = []
    my_dict = dict()
    my_set = set()
    counter = 1

    for i in list:
        if i[1] not in my_dict:
            my_dict[i[1]] = counter
        else:
            my_dict[i[1]] += 1
        print(my_dict)

        if my_dict[i[1]] >= 3:
            my_set.add(i[1])
            print(my_set)

    return my_set
        


print(spammyUsers(requests))