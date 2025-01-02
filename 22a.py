

def parse():
    file = open('22.txt')
    data = file.readlines()
    file.close()

    data = [int(line.strip()) for line in data]
    return data







def do_a_step(secret):
    mul = secret * 64
    secret = mul ^ secret
    secret = secret % 16777216

    div = secret // 32
    secret = div ^ secret
    secret = secret % 16777216
    
    mul = secret * 2048
    secret = mul ^ secret
    secret = secret % 16777216
    return secret



def del2():
    data = parse()
    lenght = len(data)
    
    scores = dict() # (change1, change2, change3, change4) -> score
    for n, old_elem in enumerate(data):
        if n % 100 == 0:
            print('On',n,'of',lenght)

        price_changes = [-1]*2000
        prices = [-1]*2000

        old_price = int(str(old_elem)[-1])

        for n in range(0,2000):
            new_elem = do_a_step(old_elem)
            new_price = int(str(new_elem)[-1])
            price_changes[n] = new_price-old_price
            prices[n]= new_price
            old_price = new_price
            old_elem = new_elem
        
        seen = dict()
        
        for n in range(3,2000):
            c1 = price_changes[n-3]
            c2 = price_changes[n-2]
            c3 = price_changes[n-1]
            c4 = price_changes[n]
            been_here = seen.get((c1,c2,c3,c4),False)
            if not been_here:
                #print('Have not seen')
                #if (-2,1,-1,3) == (c1,c2,c3,c4):
                #    print('hallå')
                seen[(c1,c2,c3,c4)] = True
                scores[(c1,c2,c3,c4)] = scores.get((c1,c2,c3,c4),0) + prices[n]
            else:
                #print('Have seen')
                pass
    
    max_value = 0
    for keys, value in scores.items():
        if value > max_value:
            max_value = value
            print('keys',keys,'value',value)



def del1():
    data = parse()
    lenght = len(data)

    score = 0
    for n, elem in enumerate(data):
        print('On',n,'of',lenght)
        for n in range(0,2000):
            elem = do_a_step(elem)
        #print(elem)
        score += elem
    print(score)


del2()