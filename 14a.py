


file = open('14.txt')
data = file.readlines()
file.close()

robots = list()
for line in data:
    dom = line.replace('p=','').replace('v=','')
    dom = dom.split()
    dom = dom[0].split(',')+dom[1].split(',')
    dom = [int(elem) for elem in dom]
    robots.append(dom)
[print(line) for line in robots ]

SMALL = False
STEPS = 100
if SMALL:
    MAPSIZE = (11,7)
else: MAPSIZE = (101,103)

quadrants_counter = [0,0,0,0]
placment = list()
for robot in robots:
    x = robot[0]+robot[2]*STEPS
    y = robot[1]+robot[3]*STEPS
    #print('after steping cords',x,y)
    x = x % MAPSIZE[0]
    y = y % MAPSIZE[1]
    #print('after mod cords',x,y)
    placment.append((x,y))
    if x != MAPSIZE[0]//2 and y != MAPSIZE[1]//2:
        if x < MAPSIZE[0]//2:
            if y < MAPSIZE[1]//2:
                quadrants_counter[0] += 1
            else:
                quadrants_counter[1] += 1
        else:
            if y < MAPSIZE[1]//2:
                quadrants_counter[2] += 1
            else:
                quadrants_counter[3] += 1
score = 1
for quadrant in quadrants_counter:
    score *= quadrant
print(score)

        

        
    




karta = [[0]*MAPSIZE[0] for _ in range(MAPSIZE[1])]
for mec in placment:
    colum = mec[0]
    row = mec[1]
    karta[row][colum] += 1
for row in karta:
    s = ''
    for elem in row:
        if elem == 0:
            s = s + '.'
        else:
            s = s + str(elem)
    #print(s)



        

