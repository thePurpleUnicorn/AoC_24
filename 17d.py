guess = (0,0,0,0,0,0,0,0,0, False)
count =   7,690,000
count = 303,000,000

import copy

file = open('17.txt')
data = file.readlines()
file.close()


#a = int(data[0].split(':')[1])
start_b = int(data[1].split(':')[1])
start_c = int(data[2].split(':')[1])
a = 0
b = start_b
c = start_c
#print(a,b,c)

program = data[4].split(':')[1]
program = program.split(',')
program = [int(elem) for elem in program]
print(program)


PROGRAM_LENGHT = len(program)
i = 0
jump = True
output = ''
current_output = 0
continue_run = True
output_list = list()

def compare(value):
    global current_output
    if value == program[current_output]:
        current_output += 1
        #print(value,True)
        return True
    return False


WHEN_COMBO = [0,2,5,6,7]
def is__combo(value):
    if value >= 5:
        return True
    if value == 0:
        return True
    if value == 2:
        return True
    return False

def combo(value):
    match value:
        case 0:
            return value
        case 1:
            return value
        case 2:
            return value
        case 3:
            return value
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
        case 7:
            return ValueError
        case _:
            raise ValueError
        
def instruct(value, operand):
    global i
    global jump
    global a
    global b
    global c
    global output
    global continue_run
    global output_list
    match value:
        case 0:
            a = a//(2**operand)
        case 1:
            b = b ^ operand
        case 2:
            b = operand % 8
        case 3:
            if a != 0:
                i = operand
                jump = False
        case 4:
            b = b ^ c
        case 5:
            var = operand%8
            output_list.append(var)
            output = output + str(operand%8) + ','
            #continue_run = compare(var)
        case 6:
            b = a//(2**operand)
        case 7:
            c = a//(2**operand)

def check(start_a,start_b,start_c, cur=0):
    global i
    global jump
    global a
    global b
    global c
    global output
    global continue_run
    global output_list
    a = start_a
    b = start_b
    c = start_c
    i = 0
    jump = True
    output = ''
    output_size = 0
    current_output = cur
    continue_run = True
    output_list = list()
    while i < PROGRAM_LENGHT and continue_run:
        ins = program[i]
        if is__combo(ins):
            op = combo(program[i+1])
        else:
            op = program[i+1]
        instruct(ins,op)
        if jump:
            i += 2
        else:
            jump = True
    return output_list

    #1000000000
#check(1000000001,0,0)

def move_back(an, bn, cn):
    b1 = bn ^ cn
    b2 = b1 ^ 6
    b3 = b2 ^ 5
    a1 = an*8+b3
    if cn == a1 // (2**b2):
        return True, a1, b3
    return False, -1, -1

def print_saved(inpo):
    for i, step in enumerate(inpo):
        print('Step',i,'=',step)
    print()

def make_you_way(pepp, inpu):
    step = pepp
    saved = copy.deepcopy(inpu)
    # Generate c guees
    an = saved[step]['a']
    bn = saved[step]['b'][3]
    for b3_guess in range(8):
        a1_guess = saved[step]['a']*8+b3_guess
        b2_guess = b3_guess ^ 5
        cn_guess = a1_guess // (2**b2_guess)
        b1 = bn ^ cn_guess
        b2 = b1 ^ 6
        if b2_guess != b2:
            continue
        else:
            pass
        b3 = b2 ^ 5
        a1 = an*8+b3
        if a1 != a1_guess:
            continue
        else:
            print('Step',step,'cn_guess',cn_guess,'works')
        if step == 0:
            print('STEP 0 an =', a1)
        else:
            saved[step-1]['a'] = a1
        saved[step]['b'] = [b3,b2,b1,bn]
        saved[step]['c'] = cn_guess
        #print_saved(saved)
        if step<15:
            out = check(an,bn,cn_guess)
            ans = program[step+1]
            print(out, '=', ans)
            if out[0] != ans:
                print('They are not the same')
                continue
        #print_saved(saved)
        make_you_way(step-1,saved)
    print('Step',step,'complete')
        






    
'''
for guess_c in range(7):
    works, new_a, new_b = move_back(0,program[-1],guess_c)
    if works:
        print(guess_c,'Works')
    #check(new_a, new_b, new_c) 
'''

base = dict()
base['a']=-1
base['b']=[-1,-1,-1,-1]
base['c']=-1
lookup = [copy.deepcopy(base) for _ in range(16)]
for i in range(16):
    #print(program[i])
    lookup[i]['b'][3] = program[i]
    #print(lookup[i]['b'][3])
lookup[-1]['a'] = 0
lookup[-1]['c'] = 0
print(lookup)


make_you_way(15, lookup)







'''
2,4,1,5,7,5,1,6,4,1,5,5,0,3,3,0
                        ¤-¤

a % 8       -> b
    b = ?
XOR 5 b     -> b
    b = ??
a // 2^b     -> c
    c = !!!
XOR 6 b     -> b
    b = ????
XOR b c     -> b
    b = ?????
out b

a // 8       -> a
    a = ?
jump to 0
----------------

b3 = a1 % 8
b2 = XOR 5 b3
cn = a1 // 2^b2
b1 = XOR 6 b2
bn = XOR b1 cn
out bn
an = a1 // 8

an = 0
bn = from program
cn = [0-7]

b1 = XOR bn cn
b2 = XOR b1 6
b3 = XOR b2 5
a1 = an*8+b3
b4 = från program
c1 = gissa och kontrollera senare (använd typ b3 och b*4 från 'förra' steget)






a(n+1) = an*8+[0,7]
b(n+1) = bn ^ an






a = a // 8
b = XOR (XOR 6 (XOR 5 (a % 8))) (a // 2^(XOR 5 (a % 8)))
c = a // 2^(XOR 5 (a % 8))





'''





                
