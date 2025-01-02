guess = ()

def print_out(mems, holes):
    mems_index = 0
    holes_index = 0
    mems_max = len(mems)
    holes_max = len(holes)
    string = ''
    while mems_index < mems_max and holes_index < holes_max:
        m_i, m_s, m_e = mems[mems_index]
        h_i, h_s = holes[holes_index]
        if m_i<h_i:
            string = string + str(m_e)*m_s
            mems_index += 1
        else:
            string = string + '.'*h_s
            holes_index += 1
    while mems_index < mems_max:
        m_i, m_s, m_e = mems[mems_index]
        string = string + str(m_e)*m_s
        mems_index += 1
    while holes_index < holes_max:
        h_i, h_s = holes[holes_index]
        string = string + '.'*h_s
        holes_index += 1
    print(string)




file = open('09.txt')
data = file.read()
file.close()

print(len(data))
data = list(data[:-1])
data = [int(elem) for elem in data]

print(data)

mems = list()  #(index, size, id)
holes = list() #(index, size)

index = 0
for i, element in enumerate(data):
    if i%2==0:
        mems.append((index, element, i//2))
    else:
        if element != 0:
            holes.append((index,element))
    index += element


print(mems)
print(holes)

print_out(mems, holes)

walkthru_mems = mems.copy()
walkthru_mems.reverse()

tot = len(walkthru_mems)
print(tot)

for index, size, id_num in walkthru_mems:
    if (id_num+1)%100==0:
        print('On',id_num,'of',tot)
    found = False
    ho_max = len(holes)
    ho_index = 0
    while not found and ho_index<ho_max:
        cur_hol_index, cur_hole_size = holes[ho_index]
        if cur_hole_size>=size:
            found=True
        else:
            ho_index += 1
    if cur_hol_index<index:
        if cur_hole_size==size:
            holes.pop(ho_index)
        else:
            holes[ho_index] = cur_hol_index+size, cur_hole_size-size

        mems_index = mems.index((index, size, id_num))
        mems[mems_index] = (cur_hol_index, size, id_num)
        mems.sort()
        holes.append((index,size))
        holes.sort()


    #print_out(mems,holes)

score = 0
for index, size, id_num in mems:
    i = index
    for _ in range(size):
        score += i*id_num
        i+=1
print(score)



