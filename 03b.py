guess = 17667303787

file = open('03.txt')
data = file.readlines()
file.close()

#[print(len(line)) for line in data]
data = ''.join(data)
#print(len(data))

#data = [line.split() for line in data]
#data = [[int(elem) for elem in line] for line in data]
#data = [X for line in data]
#print(data)

clean_data = ''
check = 'mul(aaaa,bbbb)'
check = '01234555567777'
check = '1234555567777r'

check = 'do()'
check = '0123'
check = '123r'

check = "don't()"
check = "0123456"
check = "123456r"



under_way = False
fst_number = 0
snd_number = 0
paser_placment = 0
score = 0

do_enable = True
do_placment = 0
dont_placment = 0

def stop_do():
    global do_placment
    global dont_placment
    do_placment = 0
    dont_placment = 0

def ifDigit(digit):
        stop_do()
        global paser_placment
        global fst_number
        global snd_number
        global under_way
        if paser_placment >= 4 and paser_placment <= 7:
            if paser_placment == 4:
                paser_placment = 5
                fst_number = digit
                return

            if paser_placment == 5:
                fst_number = fst_number*10 + digit
                return
            
            if paser_placment == 6:
                paser_placment = 7
                snd_number = digit
                return
            
            if paser_placment == 7:
                snd_number = snd_number*10 + digit
                return
        else:
            if under_way:
                    under_way = False
                    paser_placment = 0

for element in data:
    match element:
        case 'm':
            stop_do()
            paser_placment = 1
            if under_way:
                pass
            else:
                under_way = True
        case 'u':
            stop_do()
            if paser_placment == 1:
                paser_placment = 2
            else:
                if under_way:
                    under_way = False
                    paser_placment = 0
        case 'l':
            stop_do()
            if paser_placment == 2:
                paser_placment = 3
            else:
                if under_way:
                    under_way = False
                    paser_placment = 0
        case '(':
            if paser_placment == 3:
                paser_placment = 4
            else:
                if under_way:
                    under_way = False
                    paser_placment = 0
            
            if do_placment == 2:
                do_placment = 3
            else:
                do_placment == 0

            if dont_placment == 5:
                dont_placment = 6
            else:
                do_placment == 0

        case '0':
            ifDigit(0)
        case '1':
            ifDigit(1)
        case '2':
            ifDigit(2)
        case '3':
            ifDigit(3)
        case '4':
            ifDigit(4)
        case '5':
            ifDigit(5)
        case '6':
            ifDigit(6)
        case '7':
            ifDigit(7)
        case '8':
            ifDigit(8)
        case '9':
            ifDigit(9)

        case ',':
            stop_do()
            if paser_placment == 5:
                paser_placment = 6
            else:
                if under_way:
                    under_way = False
                    paser_placment = 0
        
        case ')':
            if paser_placment == 7:
                if do_enable:
                    score += fst_number*snd_number
                    print('mul(',fst_number,',',snd_number,')')
                paser_placment = 0
                under_way = False
            else:
                if under_way:
                    under_way = False
                    paser_placment = 0
            
            if do_placment == 3:
                do_enable = True
            else:
                do_placment == 0

            if dont_placment == 6:
                do_enable = False
            else:
                dont_placment == 0
        
        case 'd':
            if under_way:
                under_way = False
                paser_placment = 0
            
            do_placment = 1
            dont_placment = 1
        
        case 'o':
            if under_way:
                under_way = False
                paser_placment = 0
            
            if do_placment == 1:
                do_placment = 2
                dont_placment = 2
            else:
                do_placment = 0
                dont_placment = 0

        
        case 'n':
            if under_way:
                under_way = False
                paser_placment = 0
            
            if do_placment == 2:
                do_placment = 0
                dont_placment = 3
            else:
                do_placment = 0
                dont_placment = 0
        
        case "'":
            if under_way:
                under_way = False
                paser_placment = 0
            
            if dont_placment == 3:
                dont_placment = 4
            else:
                dont_placment = 0
            do_placment = 0
        
        case "t":
            if under_way:
                under_way = False
                paser_placment = 0
            
            if dont_placment == 4:
                dont_placment = 5
            else:
                dont_placment = 0
            do_placment = 0





        
        
        case _:
            stop_do()
            if under_way:
                under_way = False
                paser_placment = 0

print(score)





                