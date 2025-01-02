

file = open('12.txt')
data = file.readlines()
file.close()





data = [['.']+list(line.strip())+['.'] for line in data]
COLUMS = len(data[0])
data = [['.']*COLUMS]+data+[['.']*COLUMS]
ROWS = len(data)
[print(line) for line in data]

seen = [[False]*COLUMS for _ in data]
for line in seen:
    line[0] = True
    line[-1] = True
seen[0] = [True]*COLUMS
seen[-1] = [True]*COLUMS
[print(line) for line in seen]

DIRECTIONS = [(-1,0),(0,1),(1,0),(0,-1)]

def find_friends(symbol, i, j):
    if not seen[i][j]:
        if symbol == data[i][j]:
            seen[i][j] = True
            friends = [(i,j)]
            for div_i, div_j in DIRECTIONS:
                friends.extend(find_friends(symbol, i+div_i, j+div_j))
            return friends
        else:
            return []
    else:
        return []

def find_sides(symbol,list):
    counter = 0
    for i, j in list:
        for div_i, div_j in DIRECTIONS:
            if data[i+div_i][j+div_j] != symbol:
                counter += 1
    return counter



def find_area_and_perimiter(i,j):
    symbol = data[i][j]

    # Find all matching symbols
    plants = find_friends(symbol, i, j)
    #print(plants)

    # Calculate area and perimiter
    perimiter = find_sides(symbol, plants)
    area = len(plants)

    return area, perimiter
    

score = 0
for i, line in enumerate(data):
    for j, plant in enumerate(line):
        if not seen[i][j]:
            area, perimiter = find_area_and_perimiter(i,j)
            score += area*perimiter
print(score)
