guess = (0,0,0,0,0,0,0,0,0, False)
count = 7,690,000

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
            continue_run = compare(var)
        case 6:
            b = a//(2**operand)
        case 7:
            c = a//(2**operand)


start_a = 0
while True:
    if start_a%1000000==0: print('We are at',start_a)
    a = start_a
    b = start_b
    c = start_c
    i = 0
    jump = True
    output = ''
    output_size = 0
    current_output = 0
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
            
    if output_list == program:
        print('WE ARE DONE')
        print('Start A is',start_a)
        break

    start_a += 1



'''
a % 8       -> b
XOR b b     -> b
    b = 0
a / 2^b     -> c
    c = a
XOR b c     -> b
    b = a
XOR b c     -> b
    b = 0
out b

a / 8       -> a
    a = ?
jump to 0





'''





                
