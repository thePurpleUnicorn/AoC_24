
locks = list()
keys = list()

def parse():
    file = open('25.txt')
    data = file.read()
    items = data.split('\n\n')
    print(len(items))
    for item in items:
        sea = item.split()
        if sea[0][0] == '#':
            lock = list()
            for c in range(5):
                for r in range(7):
                    if sea[r][c] == '.':
                        lock.append(r-1)
                        break
            locks.append(lock)
            #print(lock)
        else:
            key = list()
            for c in range(5):
                for r in range(7):
                    if sea[r][c] == '#':
                        key.append(6-r)
                        break
            keys.append(key)
            #print(key)
        
def fits(lock:list, key:list):
    for c in range(5):
        if lock[c]+key[c]>5:
            return False
    return True







def del1():
    parse()
    score = 0
    for key in keys:
        for lock in locks:
            if fits(lock,key):
                score+=1
    print('Score',score)


del1()