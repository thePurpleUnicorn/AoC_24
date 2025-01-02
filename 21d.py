import functools

guess =[(175396398527088, 'your answer is too low'),
        (349738773993670, 'to high'),
        (348855618264070, 'to high')
        ]


def parse():
    file = open('21.txt')
    data = file.readlines()
    file.close()

    data = [list(line.strip()) for line in data]
    return data

LOOKUP_NUMPAD = dict()
LOOKUP_NUMPAD['A'] = (0,2)
LOOKUP_NUMPAD['0'] = (0,1)
LOOKUP_NUMPAD['1'] = (1,0)
LOOKUP_NUMPAD['2'] = (1,1)
LOOKUP_NUMPAD['3'] = (1,2)
LOOKUP_NUMPAD['4'] = (2,0)
LOOKUP_NUMPAD['5'] = (2,1)
LOOKUP_NUMPAD['6'] = (2,2)
LOOKUP_NUMPAD['7'] = (3,0)
LOOKUP_NUMPAD['8'] = (3,1)
LOOKUP_NUMPAD['9'] = (3,2)

def create_all(rows, updown, cols, leftright):
    if rows == 0 and cols == 0:
        return [[]]
    if rows == 0:
        answer = [[leftright]*cols]
        return answer
    if cols == 0:
        answer = [[updown]*rows]
        return answer
    ans1 = create_all(rows-1, updown, cols, leftright)
    ans1 = [seq + [updown] for seq in ans1]
    ans2 = create_all(rows, updown, cols-1, leftright)
    ans2 = [seq + [leftright] for seq in ans2]
    answer = ans1
    answer.extend(ans2)
    return answer

def kill_wrongs_num(start_row, start_colum, seqenses):
    correct_seqenses = list()
    for seq in seqenses:
        row = start_row
        colum = start_colum
        works = True
        for elem in seq:
            match elem:
                case '<':
                    colum += -1
                case '>':
                    colum += 1
                case 'v':
                    row += -1
                case '^':
                    row += 1
            if row == 0 and colum == 0:
                works = False
                break
        if works:
            correct_seqenses.append(seq)
    return correct_seqenses

def from_to_num(fr, to):
    fr_r, fr_c = LOOKUP_NUMPAD[fr]
    to_r, to_c = LOOKUP_NUMPAD[to]
    rows_up = to_r-fr_r
    col_right = to_c-fr_c
    if rows_up > 0:
        updown = '^'
        rows = abs(rows_up)
    else:
        updown = 'v'
        rows = abs(rows_up)
    if col_right > 0:
        leftright = '>'
        cols = abs(col_right)
    else:
        leftright = '<'
        cols = abs(col_right)
    
    all_seq = create_all(rows, updown, cols, leftright)
    #print(all_seq)
    correct_seq = kill_wrongs_num(fr_r,fr_c,all_seq)
    #print(correct_seq)
    return correct_seq

def create_sequence_num(input_seq:list):
    input_seq.insert(0,'A')
    answer_seq = [list()]
    for n in range(1,len(input_seq)):
        ans = from_to_num(input_seq[n-1], input_seq[n])
        ans = [seq + ['A'] for seq in ans]
        new_answer_seq = list()
        for past in answer_seq:
            for new in ans:
                new_answer_seq.append(past+new)
        answer_seq = new_answer_seq
    return answer_seq

LOOKUP = dict()
LOOKUP[('A','A')] = []
LOOKUP[('A','>')] = ['v']
LOOKUP[('A','v')] = ['<','v'] # correct
LOOKUP[('A','^')] = ['<']
LOOKUP[('A','<')] = ['v','<','<'] #correct
LOOKUP[('^','A')] = ['>']
LOOKUP[('^','>')] = ['v','>'] # ['>','v'] improvment 883155729600
LOOKUP[('^','v')] = ['v']
LOOKUP[('^','^')] = []
LOOKUP[('^','<')] = ['v','<']
LOOKUP[('>','A')] = ['^']
LOOKUP[('>','>')] = []
LOOKUP[('>','v')] = ['<']
LOOKUP[('>','^')] = ['<','^'] # correct
LOOKUP[('>','<')] = ['<','<']
LOOKUP[('v','A')] = ['^','>'] # ['>','^']
LOOKUP[('v','>')] = ['>']
LOOKUP[('v','v')] = []
LOOKUP[('v','^')] = ['^']
LOOKUP[('v','<')] = ['<']
LOOKUP[('<','A')] = ['>','>','^']
LOOKUP[('<','>')] = ['>','>']
LOOKUP[('<','v')] = ['>']
LOOKUP[('<','^')] = ['>','^']
LOOKUP[('<','<')] = []

toHigh = 348855618264070
checkTh= 307055584161760
print(toHigh-checkTh)

check = dict()
counter1 = 0
counter2 = 0

def magic(start,to,deepth):
    global counter1
    global counter2
    global check
    counter1 += 1
    if counter1%10==0:
        print('Counter1',counter1,'Counter2',counter2,'Procent',counter2/counter1)
    maybe = check.get((start,to,deepth),-1)
    if maybe != -1:
        counter2 += 1
        return maybe
    
    #print('start',start,'to',to,'deepth',deepth)
    if deepth == 0:
        return 1#,to
    seq = LOOKUP[(start,to)].copy()
    seq.append('A')
    seq.insert(0,'A')
    score = 0
    #total_string = ''
    for n in range(1,len(seq)):
        #points, string_part = magic(seq[n-1],seq[n],deepth-1)
        points = magic(seq[n-1],seq[n],deepth-1)
        score += points
        #total_string = total_string + string_part
    check[(start,to,deepth)] = score#, total_string
    return score#, total_string
    
    

def del2():
    data = parse()
    score = 0
    for sequence in data:
        print(''.join(sequence))
        list_of_seq = create_sequence_num(sequence.copy())
        #[print(''.join(s)) for s in list_of_seq]
        shortest_lenght = 99999999999999999
        for n, seq in enumerate(list_of_seq):
            seq.insert(0,'A')
            lenght = 0
            total_string = ''
            for n in range(1,len(seq)):
                #points, string_part = magic(seq[n-1],seq[n],2)
                points = magic(seq[n-1],seq[n],25)
                lenght += points
                #total_string = total_string + string_part
            
            #print(lenght)
            if lenght<shortest_lenght:
                shortest_lenght = lenght

        number = int(''.join(sequence[:-1]))
        print(shortest_lenght,'*',number)
        score += shortest_lenght*number

            #print(total_string)
    print(score)



del2()