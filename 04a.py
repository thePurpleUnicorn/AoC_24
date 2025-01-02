

file = open('04.txt')
data = file.readlines()
file.close()


#data = ''.join(data)
data = [list(line.strip()) for line in data]
#data = [[int(elem) for elem in line] for line in data]
#data = [X for line in data]
#print(data)
SIZE = len(data[0])
ROWS = len(data)

rows = data
colums = []
for i in range(SIZE): colums.append([line[i] for line in data])
#print(colums)
diagonals = []
for i in range(0, ROWS-3):
    line = []
    enil = []
    for j in range(0,ROWS-i):                 #DANGER
        line.append(data[i+j][j])
        enil.append(data[i+j][SIZE-1-j])
    diagonals.append(line)
    diagonals.append(enil)
#print(diagonals)
for i in range(1,SIZE-3):    
    line = []
    enil = []
    for j in range(0,SIZE-i):                 #DANGER
        line.append(data[j][i+j])
        enil.append(data[j][SIZE-1-i-j])
    diagonals.append(line)
    diagonals.append(enil)

#print(diagonals)

to_check = rows+colums+diagonals
#print(to_check)

score = 0
for line in to_check:
    for i in range(len(line)-3):        #DANGER
        bit = line[i:i+4]
        flag = False
        #print(bit)
        if bit==['X', 'M', 'A', 'S']:
            score += 1
            flag = True
        bit.reverse()
        if bit==['X', 'M', 'A', 'S']:
            score += 1
            flag = True
        if not flag:
            #print(bit)
            pass
        
print(score)



    


