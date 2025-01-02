'''
If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
'''

file = open('11.txt')
data = file.read()
file.close()


data = data.strip()
data = data.split()
data = [int(elem) for elem in data]
#print(data)

TIMES_TO_SPLIT = 75

seen = dict()            # int: the max interation left
graph = dict()           # [int] children of the number


def create_graph(number, iterations_left):
    if seen.get(number,0)>=iterations_left:
        return
    else:
        seen[number]=iterations_left
        if number == 0:
            graph[number] = [1]
            if iterations_left>0:
                create_graph(1, iterations_left-1)
            return
        lenght = len(str(number))
        if lenght%2==0:
            factor = 10**(lenght//2)
            first = number//factor
            second = number%factor
            graph[number] = [first,second]
            if iterations_left>0:
                create_graph(first, iterations_left-1)
                create_graph(second, iterations_left-1)
        else:
            graph[number] = [number*2024]
            if iterations_left>0:
                create_graph(number*2024, iterations_left-1)


for num in data:
    create_graph(num, TIMES_TO_SPLIT+1)

for node,children in graph.items():
    #print(node, children)
    continue
print(len(graph))

nr_of_children = dict() # [int]*TIMES_TO_SPLIT
for numbers in seen:
    array = [-1]*(TIMES_TO_SPLIT+1)
    array[0]=1
    nr_of_children[numbers]=array

for keys, vakues in nr_of_children.items():
    #print(keys,vakues)
    continue

check = list()

def calculate_children(number, iterations_left):
    if iterations_left == 0:
        check.append(number)
        #print(number)
        return nr_of_children[number][0]
    children = graph[number]
    if len(children)==1:
        prev = nr_of_children[children[0]][iterations_left-1]
        if prev == -1:
            sum = calculate_children(children[0],iterations_left-1)
            nr_of_children[number][iterations_left] = sum
        else: sum = prev
        if sum == -1:
            raise ValueError
        return sum
    if len(children)==2:
        first = nr_of_children[children[0]][iterations_left-1]
        if first == -1:
            first = calculate_children(children[0],iterations_left-1)
            nr_of_children[children[0]][iterations_left-1] = first
        second = nr_of_children[children[1]][iterations_left-1]
        if second == -1:
            second = calculate_children(children[1],iterations_left-1)
            nr_of_children[children[1]][iterations_left-1] = second
        if first == -1 or second == -1:
            raise ValueError
        sum = first+second
        nr_of_children[number][iterations_left] = sum
        return sum
    else:
        raise ValueError


tot = 0
for i, number in enumerate(data):
    print('On nr:',i+1)
    tot += calculate_children(number, TIMES_TO_SPLIT)
print('\n',tot)

for keys, vakues in nr_of_children.items():
    #print(keys,vakues)
    continue

#print(check)

'''
number_of_stones = dict()   # [int]*75
stones_to_iterate = list()  # (number, iteration_left)
for number in data:
    stones_to_iterate.append((number, TIMES_TO_SPLIT))

# Find number of children
while not stones_to_iterate:
    number, iterations_left = stones_to_iterate.pop(0)
    if number in seen:
        pass
    else:

        if number == 0:
            stones_to_iterate.append((1,iterations_left-1))




# Lookup answers for all


for run in range(TIMES_TO_SPLIT):
    print(run+1)
    new_data = list()
    for oldnumber in data:
        if oldnumber == 0:
            new_data.append(1)
            continue
        lenght = len(str(oldnumber))
        if lenght%2==0:
            factor = 10**(lenght//2)
            first = oldnumber//factor
            new_data.append(first)
            second = oldnumber%factor
            new_data.append(second)
        else:
            new_data.append(oldnumber*2024)
    data = new_data
    #print(data)

print(len(data))


'''