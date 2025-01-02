

file = open('05.txt')
data = file.read()
file.close()

[demands, orders] = data.split('\n\n')

demands = demands.split('\n')
demands = [line.strip() for line in demands]
demands = [[element for element in line.split('|')] for line in demands]
#print(demands)

orders = orders.split('\n')
orders = [line.strip() for line in orders]
orders = [line.split(',') for line in orders]
#print(orders)

lookup = dict()
for ord in demands:
    lookup[ord[0]]=-1
    lookup[ord[1]]=-1

score = 0
for line in orders:
    for i , elem in enumerate(line):
        lookup[elem] = i

    flag=True
    for dema in demands:
        fst = lookup[dema[0]]
        snd = lookup[dema[1]]
        if fst == -1 or snd == -1:
            continue
        if fst>snd:
            flag = False
            break
    if flag:
        index = int(len(line)/2)
        #print(line[index])
        score += int(line[index])
    
    for elem in line:
        lookup[elem] = -1

print(score)
    