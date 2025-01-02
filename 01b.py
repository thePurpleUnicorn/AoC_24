

file = open('01.txt')
data = file.readlines()
file.close()

first = []
second = []

data = [line.split() for line in data]
#print(data)
book = dict()
first = list()
for line in data:
    first.append(int(line[0]))
    fst = int(line[1])
    book[fst] = book.get(fst,0)+1

score=0
for cord in first:
    score += book.get(cord,0)*cord

print(score)








'''
pairs = zip(first,second)

lenght = 0
for i in pairs:
    lenght += abs(i[0]-i[1])
print(lenght)'''