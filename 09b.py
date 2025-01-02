guess = (6291408568030, False)


file = open('09.txt')
data = file.read()
file.close()

data = list(data)
data = [int(elem) for elem in data]

print(data)

current_point = 0
SIZE = len(data)-1
id_node = 0

#print(backwards_point)
holes = list()

fine_data = list()
while current_point<=SIZE:
    fine_data.extend([id_node]*data[current_point])
    id_node += 1
    current_point += 1

    try:
        holes.append((len(fine_data), data[current_point]))
        fine_data.extend([0]*data[current_point])
        current_point += 1
    except:
        pass

#print(fine_data)
print(holes)
#holes.sort()
#print(holes)
id_node += -1
backwards_point = len(data)-1

while backwards_point > 0:
    need = data[backwards_point]
    flag = True
    current_point = 0
    while flag and current_point<len(holes):
        index, hole_size = holes[current_point]
        if hole_size >= need:
            flag = False
            for i in range(need):
                fine_data[index+i]=id_node
            id_node-1
        current_point += 1
    backwards_point += -2

print(fine_data)



    







raw_data = []
for i, element in enumerate(data):
    if i%2==0:
        raw_data.extend([i//2]*element)
    else:
        raw_data.extend([-1]*element)

#print(raw_data)

current_point = 0
backwards_point = len(raw_data)-1

#print(raw_data[backwards_point])

moved_data = list()
while current_point <= backwards_point:
    if raw_data[current_point] == -1:
        while raw_data[backwards_point]==-1:
            backwards_point += -1
        moved_data.append(raw_data[backwards_point])
        backwards_point += -1
    else:
        moved_data.append(raw_data[current_point])
    current_point += 1
if current_point>backwards_point:
    moved_data.pop()
#print(moved_data)

score = 0
for i, elem in enumerate(moved_data):
    score += elem*i
print(score)
    

