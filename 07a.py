

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
    next1 = current_value + numbers[0]
    if works(next1, numbers[1:], ans): return True
    next2 = current_value * numbers[0]
    if works(next2, numbers[1:], ans): return True
    return False


score = 0
for i, par in enumerate(parameters):
    if works(0,par,answers[i]):
        #print(answers[i])
        score += answers[i]
print(score)

