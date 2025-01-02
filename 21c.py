import functools

#sequence



file = open('21.txt')
data = file.readlines()
file.close()

data = [list(line.strip()) for line in data]
print(data)

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

LOOKUP_DIRECTIONAL = dict()
LOOKUP_DIRECTIONAL['A'] = (1,2)
LOOKUP_DIRECTIONAL['<'] = (0,0)
LOOKUP_DIRECTIONAL['>'] = (0,2)
LOOKUP_DIRECTIONAL['v'] = (0,1)
LOOKUP_DIRECTIONAL['^'] = (1,1)

@functools.cache
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

def kill_wrongs_dir(start_row, start_colum, seqenses):
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
            if row == 1 and colum == 0:
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

def from_to_dir(fr, to):
    fr_r, fr_c = LOOKUP_DIRECTIONAL[fr]
    to_r, to_c = LOOKUP_DIRECTIONAL[to]
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
    correct_seq = kill_wrongs_dir(fr_r,fr_c,all_seq)
    #print(correct_seq)
    return correct_seq

def mix(array1:list, array2:list):
    ans = list()
    for vec1 in array1:
        for vec2 in array2:
            ans.append(vec1+vec2)
    return ans


def create_seqens_num(input_seq:list):
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


def create_seqens_dir2(input_seq:list):
    input_seq.insert(0,'A')
    answer_builder = [list()]
    for n in range(1,len(input_seq)):
        ans = from_to_dir(input_seq[n-1], input_seq[n])
        ans = [seq + ['A'] for seq in ans]
        new_answer_build = list()
        for past in answer_builder:
            for new in ans:
                new_answer_build.append(past+new)
        answer_builder = new_answer_build
    return answer_builder



def create_seqens_dir1(list_of_seqens):
    answer = list()
    lenght = len(list_of_seqens)
    for n, input_seq in enumerate(list_of_seqens):
        #print('On',n,'of',lenght)
        output_seqens = create_seqens_dir2(input_seq.copy())
        #print('Compling')
        answer.extend(output_seqens)
    return answer





def from_to_dir_lenght(fr,to):
    fr_r, fr_c = LOOKUP_DIRECTIONAL[fr]
    to_r, to_c = LOOKUP_DIRECTIONAL[to]
    rows_up = to_r-fr_r
    col_right = to_c-fr_c
    return abs(rows_up)+abs(col_right)

def find_lenght(list_of_sequens):
    lowest_lenght = 9999999
    main_list_lenght = len(list_of_sequens)
    for n, seq in enumerate(list_of_sequens):
        #print('On',n,'of',main_list_lenght)
        seq.insert(0,'A')
        seq_lenght = 0
        for n in range(1,len(seq)):
            ans = from_to_dir_lenght(seq[n-1], seq[n])
            ans += 1 #Push A for parent
            seq_lenght += ans
        if seq_lenght < lowest_lenght:
            lowest_lenght = seq_lenght
    return lowest_lenght

        



def find_smallest(list_of_seq):
    lowest = 999999
    for seq in list_of_seq:
        lenght = len(seq)
        if lenght<lowest:
            lowest = lenght
    return lowest


def check(seq, string):
    li = list(string)
    if li in seq:
        print('Found it',string)

def parser(line:list):
    s = ''.join(line[:-1])
    return int(s)

@functools.cache
def convert_directional_ketpad(seq:str):
    seq = list(seq)
    current_i, current_j = LOOKUP_DIRECTIONAL['A']
    new_seq = list()
    for elem in seq:
        new_i, new_j = LOOKUP_DIRECTIONAL[elem]
        dif_i = new_i-current_i
        dif_j = new_j-current_j
        if dif_i<0:
            new_seq.extend(['v']*(-dif_i))
        if dif_j>0:
            new_seq.extend(['>']*dif_j)
        if dif_i>0:
            new_seq.extend(['^']*dif_i)
        if dif_j<0:
            new_seq.extend(['<']*(-dif_j))
        new_seq.append('A')
        current_i = new_i
        current_j = new_j
    new_seq = ''.join(new_seq)
    return new_seq

def del2():
    score = 0
    for line in data:
        number = parser(line)
        #sequence
        sequence_list = create_seqens_num(line.copy())
        shortest_lenght = 99999999999
        for sequence in sequence_list:
            current_sequence = ''.join(sequence)
            for n in range(25):
                print('On',n,'of 25')
                print(len(current_sequence))
                current_sequence = convert_directional_ketpad(current_sequence)
            lenght = len(current_sequence)
            if lenght < shortest_lenght:
                shortest_lenght = lenght
        score += shortest_lenght*number
        #seqses2 = create_seqens_dir1(seqses1)
        #check(seqses2,'v<<A>>^A<A>AvA<^AA>A<vAAA>^A')
        #seqses3 = create_seqens_dir1(seqses2)
        #check(seqses3,'<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A')
        #size = find_smallest(seqses3)
        #size = find_lenght(seqses2)
        #print(size,'*',number,'=',size*number)
        #score += size*number
        


        #seqens = run(line)
        #temp = len(seqens)*number
        #print('Line score is',temp,'Number is',number,'Seq lenght is',len(seqens))
        #score += temp
    print(score)

del2()
