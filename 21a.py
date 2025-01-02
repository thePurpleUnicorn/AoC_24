Guess = (250812,'to high')


file = open('21.txt')
data = file.readlines()
file.close()


#data = ''.join(data)
data = [list(line.strip()) for line in data]
#data = [[int(elem) for elem in line] for line in data]
#data = [X for line in data]
print(data)

# Good keypad
# 3 bad keypads

LOOKUP_NUMPAD = dict()
LOOKUP_NUMPAD['A'] = (0,3)
LOOKUP_NUMPAD['0'] = (0,2)
LOOKUP_NUMPAD['1'] = (1,1)
LOOKUP_NUMPAD['2'] = (1,2)
LOOKUP_NUMPAD['3'] = (1,3)
LOOKUP_NUMPAD['4'] = (2,1)
LOOKUP_NUMPAD['5'] = (2,2)
LOOKUP_NUMPAD['6'] = (2,3)
LOOKUP_NUMPAD['7'] = (3,1)
LOOKUP_NUMPAD['8'] = (3,2)
LOOKUP_NUMPAD['9'] = (3,3)

LOOKUP_DIRECTIONAL = dict()
LOOKUP_DIRECTIONAL['A'] = (1,2)
LOOKUP_DIRECTIONAL['<'] = (0,0)
LOOKUP_DIRECTIONAL['>'] = (0,2)
LOOKUP_DIRECTIONAL['v'] = (0,1)
LOOKUP_DIRECTIONAL['^'] = (1,1)


def parser(line:list):
    s = ''.join(line[:-1])
    return int(s)

def convert_num_keypad(seq:list):
    current_i, current_j = LOOKUP_NUMPAD['A']
    new_seq = list()
    for elem in seq:
        new_i, new_j = LOOKUP_NUMPAD[elem]
        dif_i = new_i-current_i
        dif_j = new_j-current_j
        if dif_j<0:
            new_seq.extend(['<']*(-dif_j))
        if dif_i>0:
            new_seq.extend(['^']*dif_i)
        if dif_j>0:
            new_seq.extend(['>']*dif_j)
        if dif_i<0:
            new_seq.extend(['v']*(-dif_i))
        new_seq.append('A')
        current_i = new_i
        current_j = new_j
    return new_seq


def convert_directional_ketpad(seq:list):
    if ''.join(seq) == '^A^^<<A>>AvvvA':
        print('hallo')
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
    return new_seq
    

def run(seq:list):
    print(''.join(seq))
    seq1 = convert_num_keypad(seq)
    print(''.join(seq1))
    seq2 = convert_directional_ketpad(seq1)
    print(''.join(seq2))
    seq3 = convert_directional_ketpad(seq2)
    print(''.join(seq3))
    return seq3


score = 0
for line in data:
    number = parser(line)
    seqens = run(line)
    temp = len(seqens)*number
    print('Line score is',temp,'Number is',number,'Seq lenght is',len(seqens))
    score += temp
print(score)
