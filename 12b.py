guess = (839002, 'To LOW')

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

def find_sides(symbol,list_of_plants):
    hor = dict()
    vert = dict()
    for i, j in list_of_plants:
        if data[i +1][j ] != symbol:
            hor[i] = hor.get(i,[])+[j]
            #hor.append(i, i+1, j, None)
        if data[i -1][j ] != symbol:
            hor[i-1+ROWS] = hor.get(i-1+ROWS,[])+[j]              #might need to handel case where fence line is from top and bottom
            #hor.append(i-1, i, j, None)
        if data[i ][j +1] != symbol:
            vert[j] = vert.get(j,[])+[i]
            #vert.append(i, None, j, j+1)
        if data[i ][j -1] != symbol:
            vert[j-1+COLUMS] = vert.get(j-1+COLUMS,[])+[i]
            #vert.append(i, None, j-1, j)
    
    counter = 0
    for i, j_list in hor.items():
        j_list.sort()
        last = -1
        for elem in j_list:
            if elem!=last+1:
                counter+=1
            last = elem
    for j, i_list in vert.items():
        i_list.sort()
        last = -1
        for elem in i_list:
            if elem!=last+1:
                counter+=1
            last = elem
        


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
            print('Symbol',data[i][j],'Area', area, 'Perimiter', perimiter)
            score += area*perimiter
print(score)
