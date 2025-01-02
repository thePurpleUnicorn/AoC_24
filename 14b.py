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
#[print(line) for line in robots ]

SMALL = False
if SMALL:
    MAPSIZE = (11,7)
else: MAPSIZE = (101,103)

def take_a_step(mecs):
    new_mecs = list()
    for mec in mecs:
        x = mec[0]+mec[2]
        y = mec[1]+mec[3]
        x = x % MAPSIZE[0]
        y = y % MAPSIZE[1]
        toup = (x,y,mec[2],mec[3])
        #print(toup)
        new_mecs.append(toup)
    return new_mecs

def print_karta(macs):
    karta = [[0]*MAPSIZE[0] for _ in range(MAPSIZE[1])]
    for mec in macs:
        colum = mec[0]
        row = mec[1]
        karta[row][colum] += 1
    for y, lin in enumerate(karta):
        s = ''
        for x, elem in enumerate(lin):
            if elem == 0:
                if  x < MAPSIZE[0]//2:
                    if (MAPSIZE[0]//2-x) < (y):
                        s = s + '.'
                    else:
                        s = s + '_'
                else:
                    if (x-MAPSIZE[0]//2)<y:
                        s = s + '.'
                    else:
                        s = s + '_'
            else:
                s = s + str(elem)
        print(s)

def procent_of_chrismas(mecs):
    score = 0
    for mec in mecs:
        x = mec[0]
        y = mec[1]
        if x < MAPSIZE[0]//2:
            if (MAPSIZE[0]//2-x) < (y):
                score += 1
        else:
            if (x-MAPSIZE[0]//2)<y:
                score += 1
    procent = score/len(mecs)
    return procent

    
    
    
for i in range(100000):
    if i % 100 == 0:
        print('We are on step',i+1)
    robots = take_a_step(robots)
    grade = procent_of_chrismas(robots)
    if grade > 0.9:
        print('Step',i+1)
        print_karta(robots)
        print()


        

        
    



        

