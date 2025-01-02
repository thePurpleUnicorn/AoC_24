guess = (703, False)


file = open('02.txt')
data = file.readlines()
file.close()

data = [line.split() for line in data]
data = [[int(elem) for elem in line] for line in data]
#data = [X for line in data]
print(data)


def run_again(line):
    if line[0]>line[-1]:
        for i in range(len(line)-1):
            if line[i]-line[i+1]>=1 and line[i]-line[i+1]<=3:
                pass
            else:
                print('Unsafe')
                return False
    else:
        for i in range(len(line)-1):
            if line[i+1]-line[i]>=1 and line[i+1]-line[i]<=3:
                pass
            else:
                print('Unsafe')
                return False
    print('Safe')
    return True




def second_chance(line, i, right):
    print(line, 'line')
    line1 = line.copy()
    del line1[i]
    print(line1, 'line1')
    line2 = line.copy()
    print(line2, 'line2')
    del line2[i+1]
    if run_again(line1) or run_again(line2):
        return True
    else:
        return False

    '''
    if right:
        if line[i-1]-line[i+1]>=1 and line[i-1]-line[i+1]<=3:
            print(line, ' Old line')
            del line[i]
            print(line, 'new line')
            return run_again(line)
        
        print(line, ' Old line')
        del line[i+1]
        print(line, 'new line')
        return run_again(line)
    else:
        if line[i+1]-line[i-1]>=1 and line[i+1]-line[i-1]<=3:
            print(line, ' Old line')
            del line[i]
            print(line, 'new line')
            return run_again(line)
        
        print(line, ' Old line')
        del line[i+1]
        print(line, 'new line')
        return run_again(line)
'''

coput = 0
for line in data:
    flag = True
    if line[0]>line[-1]:
        right = True
        for i in range(len(line)-1):
            if line[i]-line[i+1]>=1 and line[i]-line[i+1]<=3:
                pass
            else:
                ans = second_chance(line,i, right)
                if ans:
                    #coput += 1
                    break
                else:
                    flag = False
                    break


                
    else:
        right = False
        for i in range(len(line)-1):
            if line[i+1]-line[i]>=1 and line[i+1]-line[i]<=3:
                pass
            else:
                ans = second_chance(line,i, right)
                if ans:
                    #coput += 1
                    break
                else:
                    flag = False
                    break


    if flag:
        coput += 1
        #print(line , ' Safe')
        pass
    else:
        #print(line, ' Nor Safe')
        pass

print(coput)

            
            


