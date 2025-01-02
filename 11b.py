from functools import cache
'''
If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
'''

seen = set()                # {int}
answers = dict()            # [0]*76
how_many_instances = dict() # [0]*76

def iterate(numbers, times_to_iterate):
    to_iterate = list()
    for number in numbers:
        if number in seen:
            instance_list = how_many_instances.get(number,[0]*76)
            instance_list[times_to_iterate]+=1
            how_many_instances[number] = instance_list
        else:
            
            to_iterate.append(number)
        
    
    

            


def how_many_numbers(number):
        if oldnumber == 0:
            new_data.append(1)
            #continue
        lenght = len(str(oldnumber))
        if lenght%2==0:
            factor = 10**(lenght//2)
            first = oldnumber//factor
            new_data.append(first)
            second = oldnumber%factor
            new_data.append(second)
        else:
            new_data.append(oldnumber*2024)


file = open('11.txt')
data = file.read()
file.close()


data = data.strip()
data = data.split()
data = [int(elem) for elem in data]
print(data)

lenght = 0
iterate(data, 75)

print(lenght)




