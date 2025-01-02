


def parse():
    file = open('23.txt')
    data = file.readlines()
    file.close()

    data = [line.strip().split('-') for line in data]
    return data

def make_conections(list_of_conections:list):
    conections = dict() # computer -> set of conections
    for computer1, computer2 in list_of_conections:
        con_set : set
        con_set = conections.get(computer1,set())
        con_set.add(computer2)
        conections[computer1] = con_set
        con_set = conections.get(computer2,set())
        con_set.add(computer1)
        conections[computer2] = con_set
    #for key, value in conections.items():
    #    value.add(key)
    return conections

def make_trio(dictionary_of_conection: dict):
    ans = dict() # computer -> all trio lan with computer
    for computer1, sets1 in dictionary_of_conection.items():
        for computer2, sets2 in dictionary_of_conection.items():
            if computer1!=computer2:
                for computer3 in sets1:
                    if computer3 in sets2:
                        group = [computer2,computer3]
                        group.sort()
                        a1 = ans.get(computer1,set())
                        a1.add(tuple(group))
                        ans[computer1] = a1

    #print()
    #print(ans)
    return ans




def make_bigger_conection(dictionary_of_touple: dict):
    ans = dict()
    for computer1, sets1 in dictionary_of_touple.items():
        for computer2, sets2 in dictionary_of_touple.items():
            if computer1!=computer2:
                for group in sets1:
                    if group in sets2:
                        group_new = list(group)
                        group_new.append(computer2)
                        group_new.sort()
                        group_new = tuple(group_new)
                        old_ans = ans.get(computer1,set())
                        old_ans.add(group_new)
                        ans[computer1] = old_ans
    return ans

                







def del2():
    data = parse()
    connections = make_conections(data)
    print('\n',connections)
    connections = make_trio(connections)
    print('\n',connections)
    for n in range(1,11):
        print('On',n)
        connections = make_bigger_conection(connections)
        #print('\n',connections)
    print('\n',connections)
    
    #score = find_longest(connections)







def del1():
    data = parse()

    conected_to = dict() # [computer] -> list of computers
    list_of_trio = set()
    for computer1, computer2 in data:
        # inizialize lists if first time
        if len(conected_to.get(computer1,[])) == 0:
            conected_to[computer1] = []
        if len(conected_to.get(computer2,[])) == 0:
            conected_to[computer2] = []

        # check for trio
        for conected_computer in conected_to[computer1]:
            if conected_computer in conected_to[computer2]:
                trio = [computer1,computer2,conected_computer]
                trio.sort()
                list_of_trio.add(tuple(trio))
        
        # connect computers
        conected_to[computer1].append(computer2)
        conected_to[computer2].append(computer1)
    
    print(list_of_trio)
    print(len(list_of_trio))

    score = 0
    for comp1, comp2, comp3 in list_of_trio:
        if comp1[0] == 't':
            score += 1
            continue
        if comp2[0] == 't':
            score += 1
            continue
        if comp3[0] == 't':
            score += 1
            continue
    print(score)

del2()