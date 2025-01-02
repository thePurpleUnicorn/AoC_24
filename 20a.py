guess=(1053814,'your answer is too high')

file = open('20.txt')
data = file.readlines()
file.close()


data = ['#'+line.strip()+'#' for line in data]
COLUMS = len(data[0])
data.insert(0,'#'*COLUMS)
data.append('#'*COLUMS)
data = [list(line) for line in data]
#[print(line) for line in data]

for i, line in enumerate(data):
    for j, elem in enumerate(line):
        if elem == 'S':
            START = (i,j,0)
        if elem == 'E':
            data[i][j]='.'
            END = (i,j)


DIV = [(1,0), (0,1), ((-1,0), (0,-1))]

lookup_clean = dict() #(i,j) = currently fastes way without ceating

places_to_study = list()
places_to_study.append(START)

while(places_to_study):
    i, j, cost = places_to_study.pop()
    past_costs = lookup_clean.get((i,j),2111333444)
    if cost < past_costs:
        # Update lowest_cost
        lookup_clean[(i,j)] = cost
        
        for k in range(4):
            if k == 0:
                if data[i-1][j] == '.':
                    places_to_study.append((i-1, j, cost+1))
            elif k == 1:
                if data[i][j+1] == '.':
                    places_to_study.append((i, j+1, cost+1))
            elif k == 2:
                if data[i+1][j] == '.':
                    places_to_study.append((i+1, j, cost+1))
            elif k == 3:
                if data[i][j-1] == '.':
                    places_to_study.append((i, j-1, cost+1))
            else:
                raise ValueError

CLEAN_RUN = lookup_clean[END]
print(lookup_clean[END])


def print_time():
    s = ''
    for i in range(len(data)):
        for j in range(COLUMS):
            var = lookup_clean.get((i,j),-1)
            if var == -1:
                s = s + '   '
            elif var < 10:
                s = s + '  ' + str(var)
            elif var < 100:
                s = s + ' ' + str(var)
            else:
                s = s + str(var)
        s = s + '\n'
    print(s)

print_time()
print('Starting jump colection')


jl = len(lookup_clean)
n = 0

score = 0
#jumps = list() # (i1,j1, i2,j2)
for i1,j1 in lookup_clean.keys():
    n += 1
    print('On',n,'of',jl)
    for i2,j2 in lookup_clean.keys():
        div_i = abs(i1-i2)
        div_j = abs(j1-j2)
        div_tot = div_i+div_j
        if div_tot<= 20:
            cost_1 = lookup_clean[(i1,j1)]
            cost_2 = lookup_clean[(i2,j2)]
            var = cost_2-cost_1+div_tot
            if var < -99:
                score += 1
                #print(var)
print(score)
'''
print('Starting scoring')
score = 0
for i1,j1, i2,j2 in jumps:
    cost_1 = lookup_clean[(i1,j1)]
    cost_2 = lookup_clean[(i2,j2)]
    var = cost_2-cost_1+2
    if var < -99:
        score += 1
        print(var)
print(score)'''