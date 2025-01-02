


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
    machine.append((int(tx),int(target[2])))

    set_list.append(machine)
    i += 4
#print(set_list)

tokens = 0
for machine in set_list:
    target_x = machine[2][0]
    target_y = machine[2][1]
    for b in range(101):
        x = machine[1][0]*b
        if x > target_x:
            continue
        y = machine[1][1]*b
        if y > target_y:
            continue
        div_x = target_x - x
        a_x = machine[0][0]
        number, rest = divmod(div_x, a_x)
        if rest != 0:
            continue
        a_y = machine[0][1]
        y = y+a_y*number
        if y != target_y:
            continue
        cost = number*3+b
        tokens += cost
        #print('a',number,'b',b,'cost',cost)
print(tokens)


            


