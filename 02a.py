
file = open('02.txt')
data = file.readlines()
file.close()

data = [line.split() for line in data]
data = [[int(elem) for elem in line] for line in data]
#data = [X for line in data]
print(data)

long=len(data[0])

coput = 0
for line in data:
    flag = True
    if line[0]>line[-1]:
        for i in range(len(line)-1):
            if line[i]-line[i+1]>=1 and line[i]-line[i+1]<=3:
                pass
            else:
                flag=False
                break
    else:
        for i in range(len(line)-1):
            if line[i+1]-line[i]>=1 and line[i+1]-line[i]<=3:
                pass
            else:
                flag=False
                break
    if flag:
        coput += 1
        #print(line , ' Safe')
    else:
        #print(line, ' Nor Safe')
        pass

print(coput)

            
            


