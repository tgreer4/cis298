import time
'''
print("Option 1 Algorithm")
start = time.time()
print(*[n for n in range(1000, 3001) if all([(int(c) % 2 == 0) for c in str(n)])], sep=',')
end = time.time()
print("Option 1 took {} seconds.\n".format(end-start))

print("Option 2 Algorithm")
start2 = time.time()
numbers = []
for i in range(1000, 3001): 
    is_even = True
    for j in str(i):
        if int(j) %2 == 1: is_even = False
    if is_even: numbers.append(i)
print(numbers)
end2 = time.time()

print("Option 2 took {} seconds.\n".format(end2-start2))

#new solution
print("Optimal Algorithm")
start = time.time()
num_list = []
for i in range(1000, 3001): 
    for j in str(i):
        if int(j[0]) % 2 == 1: 
            break
            
    else: 
        num_list.append(i)
        continue
    continue
end = time.time()
print(num_list, "\nTime of optimal algorithm is {} seconds.".format(end-start))
'''

#7-11 problem
print("Optimal Algorithm")
start = time.time()
def check_sum(self):
    sum = 0
    multiple = 0
    for a in range(len(self)):
        sum += self[a]
        multiple *= self[a]
        if(sum > 7.11 or multiple > 7.11):
            return False
    return True

price_list = []
for i in range(0, 11, 1):
    price_list.append( i / 100.0)
print(price_list)  
end = time.time()
print("\nTime of optimal algorithm is {} seconds.".format(end-start))
