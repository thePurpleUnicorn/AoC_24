guess = (1847,'to high')

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


def xmas(data, i, j):
    flag = True
    if data[i+1][j+1] == 'M':
        if data[i-1][j-1] == 'S':
            if flag:
                flag = False
            else:
                return True
    if data[i-1][j-1] == 'M':
        if data[i+1][j+1] == 'S':
            if flag:
                flag = False
            else:
                return True
    if data[i+1][j-1] == 'M':
        if data[i-1][j+1] == 'S':
            if flag:
                flag = False
            else:
                return True
    if data[i-1][j+1] == 'M':
        if data[i+1][j-1] == 'S':
            if flag:
                flag = False
            else:
                return True     
    return False

def mas(l:list):
    if l[0]=='M'and l[2]=='S':
        return True
    if l[2]=='M'and l[0]=='S':
        return True
    return False

score = 0
pour = 0
for i in range(1,ROWS-1):
    for j in range(1, SIZE-1):
        if data[i][j] == 'A':
            flag = False
            if xmas(data,i,j):
                score += 1
                flag = True
            if mas([data[i-1][j-1],data[i][j],data[i+1][j+1]]) and mas([data[i+1][j-1],data[i][j],data[i-1][j+1]]):
                pour += 1



print(score)
print(pour)


    


