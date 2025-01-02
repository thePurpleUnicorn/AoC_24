guess = (0,0,0,0,0,0,0,0,0, False)
count =   7,690,000
count = 303,000,000

import copy

file = open('17.txt')
data = file.readlines()
file.close()

START_B = 0
START_C = 0

program = data[4].split(':')[1]
program = program.split(',')
program = [int(elem) for elem in program]
print(program)
PROGRAM_LENGHT = len(program)


def check(start_a, start_step, printout = False):
    a1 = start_a

    output = list()

    for step in range(start_step,16):
        b3 = a1 % 8
        b2 = 5 ^ b3
        cn = a1 // (2**b2)
        b1 = 6 ^ b2
        bn = b1 ^ cn
        ut = bn%8
        an = a1 // 8

        if printout:
            print('out',ut,'a1',a1,'an',an,'b3',b3,'b2',b2,'b1',b1,'bn',bn,'cn',cn)
        output.append(ut)

        a1 = an
    
    return output


def backwards_step(pepp, inpu):
    if pepp == -1:
        return
    global answers

    step = pepp
    saved = copy.deepcopy(inpu)
    an = saved[step]['a']
    if an == -1:
        raise ValueError
    
    for b3_guess in range(8):
        a1_guess = an*8+b3_guess
        b2_guess = 5 ^ b3_guess
        cn_guess = a1_guess // (2**b2_guess)
        b1_guess = 6 ^ b2_guess
        bn_guess = b1_guess ^ cn_guess
        ut = bn_guess%8
        if ut != program[step]:
            continue
        else:
            print('Step',step,'a1_guess',a1_guess,'works')
        if step == 0:
            print('Found',a1_guess)
            answers.append(a1_guess)
        else:
            saved[step-1]['a'] = a1_guess
        saved[step]['b'] = [b3_guess,b2_guess,b1_guess,bn_guess]
        saved[step]['c'] = cn_guess
        #print_saved(saved)
        '''
        if step<15:
            out = check(an,step)
            ans = program[step+1]
            print(out, '=', ans)
            if out[0] != ans:
                print('They are not the same')
                continue
        '''
        #print_saved(saved)
        backwards_step(step-1,saved)
    print('Step',step,'complete')
        
#print(check(60589763,0,printout=True))

answers = list()

base = dict()
base['a']=-1
base['b']=[-1,-1,-1,-1]
base['c']=-1
lookup = [copy.deepcopy(base) for _ in range(16)]
lookup[-1]['a'] = 0
print(lookup)

backwards_step(15, lookup)





'''
2,4,1,5,7,5,1,6,4,1,5,5,0,3,3,0
                            *-*

b3 = a1%8
b2 = b3^5
cn = a1//(2**b2)
b1 = b2^6
bn = cn^b1
        out bn%8
an = a1//8

guess a1




























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
'''