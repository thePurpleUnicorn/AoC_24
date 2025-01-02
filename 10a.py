from functools import cache

@cache
def calculate_score(current_value, pos_i, pos_j):
    if KARTA[pos_i][pos_j] != current_value:
        print('WEEEWHOOOWEEEEWHHHOOOO')
    if current_value == 9:
        return {(pos_i, pos_j)}
    endpoints = set()
    for mod_i, mod_j in [(-1,0),(1,0),(0,-1),(0,1)]:
        if current_value+1==KARTA[pos_i+mod_i][pos_j+mod_j]:
            endpoints.update(calculate_score(current_value+1,pos_i+mod_i,pos_j+mod_j))
    return endpoints


def calculate_morse(current_value, pos_i, pos_j):
    if KARTA[pos_i][pos_j] != current_value:
        print('WEEEWHOOOWEEEEWHHHOOOO')
    if current_value == 9:
        return 1
    score = 0
    for mod_i, mod_j in [(-1,0),(1,0),(0,-1),(0,1)]:
        if current_value+1==KARTA[pos_i+mod_i][pos_j+mod_j]:
            score += calculate_score(current_value+1,pos_i+mod_i,pos_j+mod_j)
    return score



file = open('10.txt')
data = file.readlines()
file.close()



data = [[-1]+list(line.strip())+[-1] for line in data]
data = [[int(elem) for elem in line] for line in data]
size = len(data[0])
KARTA = [[-1]*size]+data+[[-1]*size]

[print(line) for line in KARTA]


starting_nodes = list() #[(i,j)]

for i, line in enumerate(KARTA):
    for j, elem in enumerate(line):
        if elem == 0:
            starting_nodes.append((i,j))

#print(starting_nodes)
nr_of_start = len(starting_nodes)

score = 0
for n,(i,j) in enumerate(starting_nodes):
    if n%10 == 0:
        print('Starting',n,'of', nr_of_start)
    endpoints = calculate_score(0,i,j)
    #print(endpoints)
    sprint = len(endpoints)
    #print('Sprint is',sprint)
    score += sprint
print(score)

