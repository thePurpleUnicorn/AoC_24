


file = open('18.txt')
data = file.readlines()
file.close()
data = [list(line.split(',')) for line in data]
data = [[int(elem) for elem in line] for line in data]
#print(data)

SMALL = False
if SMALL:
    SIZE = (6,6)
    FALLS = 12
else:
    SIZE = (70,70)
    FALLS = 1024


def print_map(data):
    s = ''
    for line in data:
        for elem in line:
            if elem:
                s = s + '#'
            else:
                s = s + '.'
        s = s + '\n'
    print(s)



def create_hinder(falls):
    hinder = list()
    for i in range(SIZE[0]+1):
        line = list()
        for j in range(SIZE[1]+1):
            #hinder[(i,j)] = False
            line.append(False)
            pass
        hinder.append(line)
    for n in range(falls):
        i, j = data[n]
        hinder[i][j] = True
    return hinder




WAYS = [(1,0),(0,1),(-1,0),(0,-1)]
def run(current_set : set, seen : set, obsticals:list):
    new_set = set()
    for i, j in current_set:
        for div_i, div_j in WAYS:
            new_i = i+div_i
            new_j = j+div_j
            if new_i < 0 or new_i > SIZE[0] or new_j < 0 or new_j > SIZE[1]:
                continue
            if obsticals[new_i][new_j]:
                continue
            new_pos = (new_i,new_j)
            if new_pos in seen:
                continue
            seen.add(new_pos)
            new_set.add(new_pos)
    if (SIZE[0], SIZE[1]) in new_set:
        return True
    if len(new_set)==0:
        return False
    return run(new_set,seen, obsticals)




START = {(0,0)}
top = len(data)
botom = 0
while(top-botom)>1:
    midle = (top+botom)//2
    dangers = create_hinder(midle)
    if run(START,START.copy(),dangers):
        botom = midle
    else:
        top = midle
print(top, 'gives', run(START,START.copy(),create_hinder(top)))
print(botom, 'gives', run(START,START.copy(),create_hinder(botom)))
print(data[botom])