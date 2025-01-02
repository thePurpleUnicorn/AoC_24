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

#Leta efter A
    #Hämta ut kors
    #Kolla om kors är MAS



def mas(l:list):
    if l[1]!='A':
        'WHAT THE FUCCK'
    if l[0]=='M'and l[2]=='S':
        return True
    if l[2]=='M'and l[0]=='S':
        return True
    return False

score = 0
for i in range(1,ROWS-1):
    for j in range(1,SIZE-1):
        if data[i][j]=='A':
            if mas([data[i-1][j],data[i][j],data[i+1][j]]) and mas([data[i][j-1],data[i][j],data[i][j+1]]):
                score += 1
            else:
                if mas([data[i-1][j-1],data[i][j],data[i+1][j+1]]) and mas([data[i+1][j-1],data[i][j],data[i-1][j+1]]):
                    score += 1
print(score)




    


