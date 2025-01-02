


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

tokens = 0
for machine in set_list:
    print('new')
    target_x = machine[2][0]
    target_y = machine[2][1]
    a_x = machine[0][0]
    a_y = machine[0][1]
    b_x = machine[1][0]
    b_y = machine[1][1]

    #faktor*(a_x*A+b_x*B)=target_x

    if a_x<b_x:
        is_a_x_small = True
        small_x = a_x
        big_x = b_x
    else:
        is_a_x_small = False
        small_x = b_x
        big_x = a_x
    
    max_nr_of_small, rest = divmod(target_x, small_x)
    for din in range(1000):
        if()

    for din in range(small_x):


        if (target_x-din)%small_x==0:
            print('true')










print(tokens)


            


