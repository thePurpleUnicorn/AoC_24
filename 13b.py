


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
    target_x = machine[2][0]
    target_y = machine[2][1]
    angle_target = target_x/target_y
    a_x = machine[0][0]
    a_y = machine[0][1]
    angle_a = a_x/a_y
    b_x = machine[1][0]
    b_y = machine[1][1]
    angle_b = b_x/b_y
    if angle_a>angle_b:
        low_a = True
    else: low_a = False
        
    x = b_x
    y = b_y
    nr_of_a = 0
    nr_of_b = 1
    while x<target_x and y<target_y:
        if nr_of_a%100000==0:
            print(x/target_x)
        if nr_of_b%100000==0:
            print(y/target_y)
        angle_current = x/y
        if angle_current<angle_target:
            if low_a:
                x += a_x
                y += a_y
                nr_of_a += 1
            else:
                x += b_x
                y += b_y
                nr_of_b += 1
        else:
            if not low_a:
                x += a_x
                y += a_y
                nr_of_a += 1
            else:
                x += b_x
                y += b_y
                nr_of_b += 1
    if x == target_x and y == target_y:
        tokens += nr_of_a*3+nr_of_b
    print('done')



print(tokens)


            


