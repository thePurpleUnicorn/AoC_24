

values_lookup = dict()
equations_lookup = dict()
all_z = list()

def parse():
    file = open('24.txt')
    data = file.readlines()
    file.close()

    r = 0
    while data[r] != '\n':
        line = data[r]
        line = line.split(':')
        node = line[0].strip()
        ans = bool(int(line[1]))
        values_lookup[node] = ans
        r += 1
    r += 1

    for n in range(r,len(data)):
        line = data[n].split()
        equations_lookup[line[4]] = tuple(line[:3])

        if line[4][0] == 'z':
            all_z.append(line[4])
    all_z.sort(reverse=False)

    #print(values_lookup)
    #print(equations_lookup)
    #print(all_z)

def parse2():
    file = open('24.txt')
    data = file.readlines()
    file.close()

    r = 0
    while data[r] != '\n':
        pass
        r += 1
    r += 1

    for n in range(r,len(data)):
        line = data[n].split()
        equations_lookup[line[4]] = tuple(line[:3])

        if line[4][0] == 'z':
            all_z.append(line[4])
    all_z.sort(reverse=False)

    #print(values_lookup)
    #print(equations_lookup)
    #print(all_z)

# values    dict      value of wire 
# equations dict      the equations to get a value
# all_z     list      all z values


def find_value(current_node):
    maybe_value = values_lookup.get(current_node,-1)
    if maybe_value != -1:
        return maybe_value
    
    equation = equations_lookup[current_node]
    par_node_1 = find_value(equation[0])
    par_node_2 = find_value(equation[2])
    match equation[1]:
        case 'AND':
            value = par_node_1 and par_node_2
        case 'OR':
            value = par_node_1 or par_node_2
        case 'XOR':
            value = par_node_1 != par_node_2
        case _:
            print(equation[1],'is not AND or OR or XOR')
    values_lookup[current_node] = value
    return value

def seartch(current_node):
    if current_node[0]=='x' or current_node[0]=='y':
        return [current_node]
    equation = equations_lookup[current_node]
    first_half = seartch(equation[0])
    second_half = seartch(equation[2])
    return first_half+second_half

def clear_values(lenght=44):
    global values_lookup
    values_lookup = dict()
    for n in range(lenght+1):
        if n<10:
            num = '0'+str(n)
        else:
            num = str(n)
        values_lookup['x'+num] = False
        values_lookup['y'+num] = False

def value_set(x_value,y_value):
    x_string = bin(x_value)
    x_string = x_string[2:]
    #print(x_value, '=', x_string)
    x_string = x_string[::-1]
    for n, elem in enumerate(x_string):
        if n<10:
            elem_string = 'x0'+str(n)
        else:
            elem_string = 'x'+str(n)
        if elem == '1':
            values_lookup[elem_string] = True
        else:
            values_lookup[elem_string] = False
    
    y_string = bin(y_value)
    y_string = y_string[2:]
    #print(x_value, '=', x_string)
    y_string = y_string[::-1]
    for n, elem in enumerate(y_string):
        if n<10:
            elem_string = 'y0'+str(n)
        else:
            elem_string = 'y'+str(n)
        if elem == '1':
            values_lookup[elem_string] = True
        else:
            values_lookup[elem_string] = False
        
def find_z():
    score = 0
    for pow, current_z in enumerate(all_z):
        value = int(find_value(current_z))
        #print(value,pow,value*2**pow)
        score += value*2**pow
    return score

def switch(one,two):
    ones_equation = equations_lookup[one]
    twos_equation = equations_lookup[two]
    equations_lookup[one] = twos_equation
    equations_lookup[two] = ones_equation

def del1():
    parse()
    score = 0
    for pow, current_z in enumerate(all_z):
        value = int(find_value(current_z))
        #print(value,pow,value*2**pow)
        score += value*2**pow
    print(score)

def del2():
    parse2()
    
    
    '''
    for x in range(100):
        for y in range(100):
            clear_values()
            value_set(x,y)
            z = find_z()
            if z!=(x+y):
                print(x,'+',y,'!=',z)
    '''
    switch('z12','djg')
    switch('z19','sbg')
    switch('mcq','hjm')
    switch('z37','dsd')
    
    falts = 0
    for xi in range(45):
        for yi in range(45):
            clear_values()
            value_set(2**xi,2**yi)
            if xi==0 and yi==19:
                print('hallo')
            z = find_z()
            if z!=(2**xi+2**yi):
                print(2**xi,'+',2**yi,'!=',z)
                x_s = bin(2**xi)
                x_s = ' '*(50-len(x_s))+x_s
                y_s = bin(2**yi)
                y_s = ' '*(50-len(y_s))+y_s
                z_s = bin(z)
                z_s = ' '*(50-len(z_s))+z_s
                print(x_s)
                print(y_s)
                print(z_s)
                print(xi,yi)
                falts += 1
    print(falts)

    string = ['z12','djg','z19','sbg','mcq','hjm','z37','dsd']
    string.sort()
    string = ','.join(string)
    print(string)
    
'''
    clear_values()
    value_set(7,7)
    z_value = find_z()
    print(z_value)
'''
    

    # for all z. what is touching. if only n or n-1 then good otherwise add to list
    # check good ones
    # for all bad, shuffel to fix


del2()