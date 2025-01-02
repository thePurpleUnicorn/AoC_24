


def parse():
    file = open('23.txt')
    data = file.readlines()
    file.close()

    data = [line.strip().split('-') for line in data]
    return data

def make_node_set(conections):
    nodes = set()
    for computer1, computer2 in conections:
        nodes.add(computer1)
        nodes.add(computer2)
    return nodes

def make_connections(connections:list):
    answer = dict()
    for node1, node2 in connections:
        con1 : set
        con1 = answer.get(node1,set())
        con1.add(node2)
        answer[node1] = con1
        
        con2 : set
        con2 = answer.get(node2,set())
        con2.add(node1)
        answer[node2] = con2
    return answer



# group = string = (sorted nodes joined)
group_lookup = dict() # group -> score

def find_biggest_group(group_as_list:list,connections_lookup:dict):
    global group_lookup
    group_as_string = ''.join(group_as_list)
    if group_as_string in group_lookup:
        return group_lookup[group_as_string]
    
    potential_new_members: set
    potential_new_members = connections_lookup[group_as_list[0]].copy()
    for node in group_as_list:
        pos_new_member = potential_new_members.copy()
        for potential in pos_new_member:
            if not potential in connections_lookup[node]:
                potential_new_members.remove(potential)
                
    #print('pruned_new_members', potential_new_members)
    
    max_size = len(group_as_list)
    max_group = group_as_list
    for new_member in potential_new_members:
        new_group = group_as_list.copy()
        new_group.append(new_member)
        new_group.sort()
        ans_size, ans_group = find_biggest_group(new_group,connections_lookup)
        if ans_size > max_size:
            max_size = ans_size
            max_group = ans_group
    
    group_lookup[group_as_string] = max_size, max_group
    return max_size, max_group

    







def del2():
    data = parse()
    node_set = make_node_set(data)
    connections = make_connections(data)

    lenght = len(node_set)
    print('LEGHT',lenght)
    max_size = 0
    biggest_group = None
    for n, node in enumerate(node_set):
        print('On',n,'of',lenght-1)
        size, ans_group = find_biggest_group([node],connections)
        if size > max_size:
            max_size = size
            biggest_group = ans_group
    print(max_size)
    print(biggest_group)

    s = ','.join(biggest_group)
    print(s)






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