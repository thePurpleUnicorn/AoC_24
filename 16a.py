

file = open('16.txt')
data = file.readlines()
file.close()


#data = ''.join(data)
data = [list(line.strip()) for line in data]
#data = [[int(elem) for elem in line] for line in data]
#data = [X for line in data]

START = (len(data)-2,1,0,1)           # (i, j, cost, direction)
END = (1, len(data[0])-2)
data[START[0]][START[1]] = 'X'
data[END[0]][END[1]] = '.'

[print(''.join(line)) for line in data]

places_to_study = list()
places_to_study.append(START)

lowest_cost = dict() # Key is (i,j,direction), Value is cost


while(places_to_study):
    i, j, cost, direction,  = places_to_study.pop()
    past_costs = lowest_cost.get((i,j),[2111333444,2111333444,2111333444,2111333444])
    if cost < past_costs[direction]:
        # Update lowest_cost
        new_costs = [0]*4
        new_places = set()
        new_places.add(direction)
        for k in range(4):
            if cost+1000 < past_costs[k]:
                new_costs[k]=cost+1000
                new_places.add(k)
            else: 
                new_costs[k]=past_costs[k]
        new_costs[direction] = cost
        lowest_cost[(i,j)] = new_costs

        # Take steps
        for k in new_places:
            if k == 0:
                if data[i-1][j] == '.':
                    places_to_study.append((i-1, j, new_costs[k]+1, k))
            elif k == 1:
                if data[i][j+1] == '.':
                    places_to_study.append((i, j+1, new_costs[k]+1, k))
            elif k == 2:
                if data[i+1][j] == '.':
                    places_to_study.append((i+1, j, new_costs[k]+1, k))
            elif k == 3:
                if data[i][j-1] == '.':
                    places_to_study.append((i, j-1, new_costs[k]+1, k))
            else:
                raise ValueError
            
print(lowest_cost[END])

check_set = set()
mark = 0
def colect_best_paths(i,j,dir,cost): # Return: (BOOL, SCORE) TRUE if part of best path
    global mark
    if i == 1 and j == 8:
        print('end')
    control_costs = lowest_cost.get((i,j),[-1,-1,-1,-1])
    if control_costs[dir] == cost:
        if (i,j) == END:
            if cost == min(control_costs):
                mark += 1
                check_set.add((i,j))
                return True, 1
            else:
                return False, 42
        if dir == 0:
            ans0 = colect_best_paths(i-1, j, dir, cost+1)
        else:
            ans0 = colect_best_paths(i-1, j, 0, cost+1001)
        if dir == 1:
            ans1 = colect_best_paths(i, j+1, dir, cost+1)
        else:
            ans1 = colect_best_paths(i, j+1, 1, cost+1001)
        if dir == 2:
            ans2 = colect_best_paths(i+1, j, dir, cost+1)
        else:
            ans2 = colect_best_paths(i+1, j, 2, cost+1001)
        if dir == 3:
            ans3 = colect_best_paths(i, j-1, dir, cost+1)
        else:
            ans3 = colect_best_paths(i, j-1, 3, cost+1001)
        
        score = 0
        if ans0[0]:
            score += ans0[1]
        if ans1[0]:
            score += ans1[1]
        if ans2[0]:
            score += ans2[1]
        if ans3[0]:
            score += ans3[1]
        if any((ans0[0],ans1[0],ans2[0],ans3[0])):
            mark += 1
            check_set.add((i,j))
            return True, score+1
        else:
            return False, -1000000
    else:
        return False, -2000000

print(colect_best_paths(START[0], START[1], START[3], START[2]))
print(mark)
print(len(check_set))

for i, j in check_set:
    data[i][j] = 'O'
[print(''.join(line)) for line in data]

