guess = (6291408568030, False), (6291146824486, True)


file = open('09.txt')
data = file.read()
file.close()

data = list(data)
data = [int(elem) for elem in data]

print(data)

raw_data = []
for i, element in enumerate(data):
    if i%2==0:
        raw_data.extend([i//2]*element)
    else:
        raw_data.extend([-1]*element)

print(raw_data)




backwards_point = len(raw_data)-1
moved_data = raw_data.copy()
end = False
while not end:
    if raw_data[backwards_point] == -1:
        backwards_point += -1
    else:
        id_node = raw_data[backwards_point]
        size = 0
        while raw_data[backwards_point]==id_node:
            size += 1
            backwards_point += -1
        
        forward_point = 0
        while 
        












'''
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
print(moved_data)
'''
score = 0
for i, elem in enumerate(moved_data):
    score += elem*i
print(score)
    

