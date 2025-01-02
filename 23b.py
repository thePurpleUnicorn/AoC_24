


def parse():
    file = open('23.txt')
    data = file.readlines()
    file.close()

    data = [line.strip().split('-') for line in data]
    return data



def del2():
    data = parse()
    lookup = dict() # computer -> [lans]    lans = {computer}
    for computer1, computer2 in data:
        lans1: list
        lans2: list
        lans1 = lookup.get(computer1,[])
        lans2 = lookup.get(computer2,[])

        lan1: set
        lan2: set
        to_change1 = list()
        to_change2 = list()
        for lan1 in lans1:
            for lan2 in lans2:
                if lan1==lan2:
                    #expand
                    to_change1.append(lan1)
                    to_change2.append(lan2)
                    #lan1.add(computer2)
                        #lans1.append(lan1)
                        #lookup[computer1] = lans1
                    
                    #lan2.add(computer1)
                        #lans2.append(lan2)
                        #lookup[computer2] = lans2
        for lan in to_change1:
            lan.add(computer2)
            #lans1.append(lan)
            #lookup[computer1] = lans1
        for lan in to_change2:
            lan.add(computer1)
            #lans2.append(lan)
            #lookup[computer2] = lans2

        lans1.append({computer2})
        lookup[computer1] = lans1
        
        lans2.append({computer1})
        lookup[computer2] = lans2
    
    max_lenght = 0
    master_key = ''
    master_set = None
    for key, value in lookup.items():
        for lan in value:
            if len(lan)>max_lenght:
                master_key = key
                master_set = lan
                max_lenght = len(lan)
    
    print(max_lenght)
    print(master_key,master_set)







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