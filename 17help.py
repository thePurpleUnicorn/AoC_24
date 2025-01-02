def top_and_low():
    top_value = 1000*1000*1000*1000*281
    low_value = 1000*1000*1000*1000*35
    value = 1000*1000*1000*1000*35.1

    file = open('17.txt')
    data = file.readlines()
    file.close()

    program = data[4].split(':')[1]
    program = program.split(',')
    program = [int(elem) for elem in program]
    print(program)

    dou = len(program)
    print(dou)

    for i in range(dou-1):
        value = value // 8
    print(value)


    low = 1
    for i in range(16):
        low*8**16

    print(low_value)
    print(107413700225434)
    print(top_value)

def revers_XOR():
    a = 10
    b = 5

    c = a ^ b
    print('a', c ^ b, a)
    print('b', c ^ a, b)

def XOR():
    for i in range(7):
        print('XOR 5',i,'=',i^5)

top_and_low()