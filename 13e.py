


file = open('13.txt')
data = file.readlines()
file.close()

set_list = []
i=0
while i < len(data)-1:
    machine = []
    a = data[i].split('+')
    ax = a[1].split(',')[0]
    machine.append((int(ax),int(a[2])))

    b = data[i+1].split('+')
    bx = b[1].split(',')[0]
    machine.append((int(bx),int(b[2])))

    target = data[i+2].split('=')
    tx = target[1].split(',')[0]
    machine.append((int(tx)+10000000000000,int(target[2])+10000000000000))

    set_list.append(machine)
    i += 4
#print(set_list)


def find_primes(nr):
    #print('in primes, target is',nr)
    temp_primes = dict()
    count = 2
    while count*count<=nr:
        if nr%count==0:
            temp_primes[count] = temp_primes.get(count,0)+1
            nr = nr//count
            #print('found',count,'nr is now',nr,'end will be',nr**0.5)
        else:
            count+=1
    temp_primes[nr]=1
    return temp_primes

LENGHT = len(set_list)

tokens = 0
for i, machine in enumerate(set_list):
    target_x = machine[2][0]
    target_y = machine[2][1]
    a_x = machine[0][0]
    a_y = machine[0][1]
    b_x = machine[1][0]
    b_y = machine[1][1]


    B, rest = divmod(target_x*a_y-target_y*a_x,  b_x*a_y-b_y*a_x)
    if rest != 0:
        continue
    #print('rest',rest)
    #print('B =',B)

    A , rest = divmod(target_x-B*b_x, a_x)
    if rest != 0:
        print('We are here')
        print('i:',i,'Row',i*4+1)
        print('We are done')
        continue
    
    cost = A*3+B
    #print('For',i,'of',LENGHT,': A',A,'B',B,'cost',cost)
    tokens += cost

print(tokens)