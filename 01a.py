

file = open('01.txt')
data = file.readlines()
file.close()

first = []
second = []

data = [line.split() for line in data]
#print(data)

first = [int(line[0]) for line in data]
second = [int(line[1]) for line in data]

first.sort()
second.sort()

print(first)
print(second)

pairs = zip(first,second)

lenght = 0
for i in pairs:
    lenght += abs(i[0]-i[1])
print(lenght)