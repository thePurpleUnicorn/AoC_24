


def parse():
    file = open('23.txt')
    data = file.readlines()
    file.close()

    data = [line.strip().split('-') for line in data]
    return data


#list_of_computers = list()
lan_lookup = dict() # [computer] -> (lan_id)
computer_lookup = dict() # [lan_id] -> computers conected to lan_id 
next_lan_id = 0




def del1():
    global lan_lookup
    global computer_lookup
    global next_lan_id
    data = parse()
    for computer1, computer2 in data:
        lan1 = lan_lookup.get(computer1, -1)
        lan2 = lan_lookup.get(computer2, -1)
        if lan1 == -1:
            if lan2 == -1:
                lan_lookup[computer1] = next_lan_id
                lan_lookup[computer2] = next_lan_id
                computer_lookup[next_lan_id] = [computer1,computer2]
                next_lan_id += 1
                continue
            else:
                lan_lookup[computer1] = lan2
                computer_lookup[lan2].append(computer1)
                continue
        else:
            if lan2 == -1:
                lan_lookup[computer2] = lan1
                computer_lookup[lan1].append(computer2)
                continue
            else:
                if lan1 == lan2:
                    continue
                if lan1 < lan2:
                    computers_to_move = computer_lookup[lan2]
                    computer_lookup[lan1].extend(computers_to_move)
                    computer_lookup.pop(lan2)
                    for comp in computers_to_move:
                        lan_lookup[comp] = lan1
                    continue
                else:
                    computers_to_move = computer_lookup[lan1]
                    computer_lookup[lan2].extend(computers_to_move)
                    computer_lookup.pop(lan1)
                    for comp in computers_to_move:
                        lan_lookup[comp] = lan2
                    continue
    print(lan_lookup)





del1()