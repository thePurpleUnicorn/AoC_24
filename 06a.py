
def print_out(been_here, map):
    drawing = [[' ']*COLUMS for _ in map]
    for i in range(ROWS):
        for j in range(COLUMS):
            if been_here[i][j]:
                drawing[i][j] = 'X'
            else:
                drawing[i][j] = map[i][j]
    [print(''.join(line)) for line in drawing]
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

[print(line) for line in map]

been_here = [[False]*COLUMS for _ in map]
[print(line) for line in been_here]

UP = 4
RIGHT = 1
DOWN = 2
LEFT = 3

direction = UP
while i >= 1 and i < ROWS-1 and j >= 1 and j < COLUMS-1:
    match direction:
        case 4:
            if map[i-1][j]=='#':
                direction = RIGHT
            else:
                i += -1
                been_here[i][j] = True
        case 1:
            if map[i][j+1]=='#':
                direction = DOWN
            else:
                j += 1
                been_here[i][j] = True
        case 2:
            if map[i+1][j]=='#':
                direction = LEFT
            else:
                i += 1
                been_here[i][j] = True
        case 3:
            if map[i][j-1]=='#':
                direction = UP
            else:
                j += -1
                been_here[i][j] = True
    #print_out(been_here, map)
    #print()

print_out(been_here, map)

score = 0
for x in range(ROWS):
    for y in range(COLUMS):
        if been_here[x][y]:
            score += 1

print(score)

