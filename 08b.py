

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

def create_antinodes(start_i, start_j, distans_i, distans_j):
    next_i = start_i+distans_i
    next_j = start_j+distans_j
    if next_i < 0 or next_i > ROWS-1 or next_j < 0 or next_j  > COLUMS-1:
        return
    else:
        antinodes.add((next_i, next_j))
        create_antinodes(next_i, next_j, distans_i, distans_j)



for values in placments.values():
    for i, cord1 in enumerate(values):
        for j, cord2 in enumerate(values):
            if i>j:
                i_dif = cord2[0] - cord1[0]
                j_dif = cord2[1] - cord1[1]
                right_i = cord2[0]+i_dif
                right_j = cord2[1]+j_dif
                left_i = cord1[0]-i_dif
                left_j = cord1[1]-j_dif
                create_antinodes(cord1[0],cord1[1],i_dif,j_dif)
                create_antinodes(cord2[0],cord2[1],-i_dif,-j_dif)

print(len(antinodes))



