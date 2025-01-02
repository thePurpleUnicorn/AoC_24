


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
print(set_list)


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



tokens = 0
for machine in set_list:
    target_x = machine[2][0]
    target_y = machine[2][1]
    #print('targets',target_x,target_y)
    a_x = machine[0][0]
    a_y = machine[0][1]
    b_x = machine[1][0]
    b_y = machine[1][1]
    #faktor*(a_x*A+b_x*B)=target_x


    primes_x = find_primes(target_x)
    primes_y = find_primes(target_y)
    print('primes'), print(primes_x), print(primes_y)


    done = False

    for A in range(1,1000):
        for B in range(1,1000):
            number, rest = divmod(target_x, a_x*A+b_x*B)
            if rest == 0:
                faktor = number
                if target_y == faktor*(a_y*A+b_y*B):
                    cost = (A*3+B)*faktor
                    tokens += cost
                    print('As',A*faktor,'Bs',B*faktor,'cost',cost)
                    done = True
                    break
                else:
                    break
        if done:
            break

print(tokens)