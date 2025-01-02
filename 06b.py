
def print_out(been_here, map):
    drawing = [[' ']*COLUMS for _ in map]
    for i in range(ROWS):
        for j in range(COLUMS):
            s = 0
            for d in range(4):
                #print(been_here[i][j])
                if been_here[i][j][d]:
                    s+=d+1
            if s>0:
                drawing[i][j] = str(s)
            else:
                drawing[i][j] = map[i][j]
    hej = [''.join(line) for line in drawing]
    #print(hej)
    prime = ''
    for line in hej:
        prime = prime + line + '\n'
    print(prime)
    return hej
    #[print(line) for line in been_here]

    



file = open('06.txt')
data = file.readlines()
file.close()


map = [list(line.strip()) for line in data]
COLUMS = len(map[0])
ROWS = len(map)
flag = False
for i in range(ROWS):
    if flag:
        break
    for j in range(COLUMS):
        if map[i][j]=='^':
            pos_i = i
            pos_j = j
            map[i][j]='.'
            flag = True
            break

i = pos_i
j = pos_j

#[print(line) for line in map]



UP = 4
RIGHT = 1
DOWN = 2
LEFT = 3
direction = UP

score = 0
for x in range(ROWS):
    print('Row',x,'of',ROWS)
    for y in range(COLUMS):
        if pos_i==x and pos_j==y:
            continue
        elif map[x][y]=='#':
            continue
        elif map[x][y]=='.':
            map[x][y]='#'
            been_here = [[[False,False,False,False] for _ in line] for line in map]

            #print_out(been_here,map)
            
            #been_here = []
            #been_here = [[ [False for _ in range(4)] for _ in range(COLUMS)] for _ in range(ROWS)]
            '''
            for a in range(ROWS):
                r = []
                for b in range(COLUMS):
                    r.append([False,False,False,False])
                been_here.append(r)
                '''

            loop = False
            i = pos_i
            j = pos_j
            direction = UP
            while i >= 1 and i < ROWS-1 and j >= 1 and j < COLUMS-1:
                match direction:
                    case 4:
                        if map[i-1][j]=='#':
                            direction = RIGHT
                        else:
                            i += -1
                            if been_here[i][j][direction-1]:
                                loop = True
                                break
                            else:
                                been_here[i][j][direction-1] = True
                    case 1:
                        if map[i][j+1]=='#':
                            direction = DOWN
                        else:
                            j += 1
                            if been_here[i][j][direction-1]:
                                loop = True
                                break
                            else:
                                been_here[i][j][direction-1] = True
                    case 2:
                        if map[i+1][j]=='#':
                            direction = LEFT
                        else:
                            i += 1
                            if been_here[i][j][direction-1]:
                                loop = True
                                break
                            else:
                                been_here[i][j][direction-1] = True
                    case 3:
                        if map[i][j-1]=='#':
                            direction = UP
                        else:
                            j += -1
                            if been_here[i][j][direction-1]:
                                loop = True
                                break
                            else:
                                been_here[i][j][direction-1] = True
            #print_out(been_here,map)
            #print('------------------')
            map[x][y]='.'
            if loop:
                score += 1
                




    #print_out(been_here, map)
    #print()

#print_out(been_here, map)

print(score)

