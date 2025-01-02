

file = open('08.txt')
data = file.readlines()
file.close()


#data = ''.join(data)
map = [line.strip() for line in data]
#data = [[int(elem) for elem in line] for line in data]
#data = [X for line in data]
#print(data)
ROWS = len(map)
COLUMS = len(map[0])

symbols = set()
placments = dict()

for i, line in enumerate(map):
    for j, elem in enumerate(line):
        if elem != '.':
            symbols.add(elem)
            placments[elem] = list()

#print(symbols)

for i, line in enumerate(map):
    for j, elem in enumerate(line):
        if elem != '.':
            placments[elem].append((i,j))

#print(placments)

antinodes = set()

for values in placments.values():
    for i, cord1 in enumerate(values):
        for j, cord2 in enumerate(values):
            if i>j:
                if cord1 != cord2:
                    i_dif = cord2[0] - cord1[0]
                    j_dif = cord2[1] - cord1[1]
                    right_i = cord2[0]+i_dif
                    right_j = cord2[1]+j_dif
                    left_i = cord1[0]-i_dif
                    left_j = cord1[1]-j_dif
                    if right_i < 0 or right_i > ROWS-1 or right_j < 0 or right_j  > COLUMS-1:
                        pass
                    else:
                        antinodes.add((right_i, right_j))
                    if left_i < 0 or left_i > ROWS-1 or left_j < 0 or left_j  > COLUMS-1:
                        pass
                    else:
                        antinodes.add((left_i, left_j))

print(len(antinodes))



