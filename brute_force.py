from simon import *
import random

num_rounds = 2
keys = []
for i in range(num_rounds):
    keys.append(random.randint(0,2**WS-1))

print("Keys: ")
print(keys)
possible = []
for k1 in range(2**WS):
    for k2 in range(2**WS):
        possible.append([k1,k2])
        
print("HI")
while len(possible) > 1:
    new = []
    for pair in possible:
        b = random.randint(0,2**(2*WS)-1)
        if(simon(b, pair, 2) == simon(b, keys, 2)):
            new.append(pair)
    possible = new

print(possible)
        
