import math
import time


file = open('07.txt')
data = file.readlines() #file.read()
file.close()


data = [line.strip() for line in data]
answers = list()
parameters = list()
for line in data:
    [ans, par] = line.split(':')
    answers.append(int(ans))
    par = par.split()
    parameters.append([int(elem) for elem in par])
#print(answers)

def works(current_value, numbers:list, ans):
    if len(numbers) == 0:
        if current_value == ans: return True
        else: return False
    if current_value>ans: return False                      # MARK 2
    next_number = numbers[0]                                # MARK 3
    rest = numbers[1:]                                      # MARK 3
    next1 = current_value + next_number
    if works(next1, rest, ans): return True
    next2 = current_value * next_number
    if works(next2, rest, ans): return True
    multipler = 10**(int(math.log10(next_number))+1)
    next3 = current_value*multipler + next_number
    if works(next3, rest, ans): return True
    return False


start_time = time.time()

score = 0
for i, par in enumerate(parameters):
    if works(par[0],par[1:],answers[i]):                # MARK 1
        #print(answers[i])
        score += answers[i]
print(score)

print('Time:', time.time()-start_time)