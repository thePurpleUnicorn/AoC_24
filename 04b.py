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
    if i == 0 or j==0 or i==ROWS-1 or j==SIZE-1:
        return False
    flag = True
    if data[i-1][j] == 'M':
        if data[i+1][j] == 'S':
            if flag:
                flag = False
            else:
                pass
                #return True
    if data[i+1][j] == 'M':
        if data[i-1][j] == 'S':
            if flag:
                flag = False
            else:
                pass
                #return True
    if data[i][j+1] == 'M':
        if data[i][j-1] == 'S':
            if flag:
                flag = False
            else:
                pass
                #return True
    if data[i][j-1] == 'M':
        if data[i][j+1] == 'S':
            if flag:
                flag = False
            else:
                pass
                #return True
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



score = 0
for i in range(ROWS):
    for j in range(SIZE):
        #if i == 4 and (j == 2 or j == 4):
            #print('hej')
        if data[i][j] == 'A':
            if xmas(data,i,j):
                score += 1
'''

                bit = list()
                for a in [i-1,i,i+1]:
                    pi = list()
                    for b in [j-1,j,j+1]:
                        if (data[a][b]=='A' or data[a][b]=='X') and (a != i or b != j):
                            pi.append('.')
                        else:
                            pi.append(data[a][b])
                    bit.append(''.join(pi))
                #[print(c) for c in bit]
                #print()

                bit = list()
                for a in [i-1,i,i+1]:
                    pi = list()
                    for b in [j-1,j,j+1]:
                        pi.append(data[a][b])
                    bit.append(pi)
                if not xmas(bit,1,1):
                    print('DANGER')
'''


print(score)



    


