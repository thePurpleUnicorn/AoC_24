

file = open('15.txt')
data = file.readlines()
file.close()


karta = list()
i = 0
while data[i][0] == '#':
    line = list()
    for j, elem in enumerate(data[i]):
        if elem == '@':
            START = i,j*2
            line.extend(['.','.'])
        elif elem == '\n':
            pass
        elif elem == 'O':
            line.extend(['[',']'])
        else:
            line.extend([elem,elem])
    karta.append(line)
    i+=1
i += 1

directions = list()
for line in range(i,len(data)):
    directions.extend(list(data[line].strip()))

def print_karta(ka, pos_i, pos_j):
    s = ''
    for i, line in enumerate(ka):
        for j, elem in enumerate(line):
            if pos_i == i and pos_j == j:
                s = s + '@'
            else: s = s + elem
        s = s + '\n'
    return s

print(print_karta(karta,START[0],START[1]))
#print(directions)

def try_push(i,j,dir):
    current = karta[i][j]
    match current:
        case '#':
            return False, None
        
        case '.':
            return True, []
        
        case ']':
            if dir[1] == 0:
                movers = list()
                b1, movers1 = try_push(i+dir[0],j+dir[1],dir)
                b2, movers2 = try_push(i+dir[0],j+dir[1]-1,dir)
                if b1 and b2:
                    movers.extend(movers1)
                    movers.extend(movers2)
                    movers.extend([(i,j,']'), (i,j-1,'[')])
                    return True, movers
                else:
                    return False, None
            else:
                b1, movers1 = try_push(i+dir[0],j+dir[1],dir)
                if b1:
                    movers1.append((i,j,']'))
                    return True, movers1
                else:
                    return False, None
                
        case '[':
            if dir[1] == 0:
                movers = list()
                b1, movers1 = try_push(i+dir[0],j+dir[1],dir)
                b2, movers2 = try_push(i+dir[0],j+dir[1]+1,dir)
                if b1 and b2:
                    movers.extend(movers1)
                    movers.extend(movers2)
                    movers.extend([(i,j,'['), (i,j+1,']')])
                    return True, movers
                else:
                    return False, None
            else:
                b1, movers1 = try_push(i+dir[0],j+dir[1],dir)
                if b1:
                    movers1.append((i,j,'['))
                    return True, movers1
                else:
                    return False, None
            
        case _:
            raise ValueError
        
def update_map(moves, dir):
    for move in moves:
        karta[move[0]][move[1]] = '.'
    for move in moves:
        karta[move[0]+dir[0]][move[1]+dir[1]] = move[2]

        
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
    
    bo, movers = try_push(pos_i+dir[0], pos_j+dir[1], dir)
    if bo:
        movers.append((pos_i,pos_j,'.'))
        update_map(movers, dir)
        pos_i += dir[0]
        pos_j += dir[1]
    
    #print(print_karta(karta,pos_i,pos_j))




score = 0
for i, line in enumerate(karta):
    for j, elem in enumerate(line):
        if elem == '[':
            score += i*100+j
print(score)
