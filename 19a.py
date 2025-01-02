import functools


file = open('19.txt')
data = file.readlines()
file.close()

towels = data[0].split(',')
towels = [elem.strip() for elem in towels]
print(towels)

patterns = data[2:]
patterns = [elem.strip() for elem in patterns]
print(patterns)

def match_string(pat, tow):
    if len(pat)<len(tow):
        return False
    for n in range(len(tow)):
        if pat[n] != tow[n]:
            return False
    return True 

@functools.cache
def look_for_pattern(patt):
    counter = 0
    if len(patt) == 0:
        return 1
    for towel in towels:
        if match_string(patt, towel):
            new_patt = patt[len(towel) : ]
            to_add = look_for_pattern(new_patt)
            counter += to_add
    return counter

import time

start =  time.time()
score = 0
for pattern in patterns:
    to_add = look_for_pattern(pattern)
    tid = time.time() - start
    print(tid)
    score += to_add 
print(score)