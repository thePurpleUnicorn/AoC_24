

file = open('15.txt')
data = file.readlines()
file.close()


karta = list()
k = 0
while data[k][0] == '#':
    karta.append(list(data[k].strip()))
    k += 1
k += 1
flag = False
for i, line in enumerate(karta):
    for j, elem in enumerate(line):
        if elem == '@':
            START = i,j
            karta[i][j]='.'
            flag = True
    if flag: break

directions = list()
for line in range(k,len(data)):
    directions.extend(list(data[line].strip()))

def print_karta(ka, pos_i, pos_j):
    s = ''
    for i, line in enumerate(karta):
        for j, elem in enumerate(line):
            if pos_i == i and pos_j == j:
                s = s + '@'
            else: s = s + elem
        s = s + '\n'
    return s

#print_karta(karta)
#print(directions)

def try_push(i,j,dir):
    current = karta[i][j]
    match current:
        case '#':
            return False
        case '.':
            return True
        case 'O':
            if try_push(i+dir[0],j+dir[1],dir):
                karta[i+dir[0]][j+dir[1]] = 'O'
                return True
            else:
                return False
        case _:
            raise ValueError
        
pos_i = START[0]
pos_j = START[1]
for move in directions:
    match move:
        case '<':
            dir = (0,-1)
        case '>':
            dir = (0,1)
        case '^':
            dir = (-1,0)
        case 'v':
            dir = (1,0)

    if try_push(pos_i+dir[0], pos_j+dir[1], dir):
        pos_i += dir[0]
        pos_j += dir[1]
        karta[pos_i][pos_j] = '.'

score = 0
for i, line in enumerate(karta):
    for j, elem in enumerate(line):
        if elem == 'O':
            score += i*100+j
print(score)