guess = (0,0,0,0,0,0,0,0,0, False)

file = open('17.txt')
data = file.readlines()
file.close()


a = int(data[0].split(':')[1])
b = int(data[1].split(':')[1])
c = int(data[2].split(':')[1])
#print(a,b,c)

program = data[4].split(':')[1]
program = program.split(',')
program = [int(elem) for elem in program]
print(program)

PROGRAM_LENGHT = len(program)
i = 0
jump = True
output = ''

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
            return None
        case _:
            raise ValueError
        
def instruct(value, operand):
    global i
    global jump
    global a
    global b
    global c
    global output
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
            output = output + str(operand%8) + ','
        case 6:
            b = a//(2**operand)
        case 7:
            c = a//(2**operand)

while i < PROGRAM_LENGHT:
    if i == 0:
        print('Run it again')
    ins = program[i]
    if is__combo(ins):
        op = combo(program[i+1])
    else:
        op = program[i+1]
    instruct(program[i],op)
    if jump:
        i += 2
    else:
        jump = True

print('A', a)
print('B', b)
print('C', c)
output = output.removesuffix(',')
print(output)



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





                
