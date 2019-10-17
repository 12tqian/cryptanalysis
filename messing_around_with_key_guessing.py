from util import *
from simon import *
from random import randint



#try to break 3 rounds
#At round 0, diff is (0, d{6})
startdiff = [0,convert2([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])]

#At round 2, diff is (d{8},d{6})
enddiff = [convert2([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]),convert2([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])]
NC = 1000 #Number of pair candidates

def rand_word(size = WS):
    return randint(0,2**(WS)-1)

keys = [rand_word(),rand_word(),rand_word(),rand_word()]
print(keys)
#Generate a bunch of pair candidates
pairs = []
for count in range(NC):
    left1, right1 = rand_word(), rand_word()
    left2, right2 = left1^startdiff[0], right1^startdiff[1]
    pairs.append([compose(left1,right1),compose(left2,right2)])

#Pair filtering
filtered = []
for pair in pairs:
        out1 = simon(pair[0],keys,rounds=4)
        outleft1, outright1 = split(out1)
        out2 = simon(pair[1],keys,rounds=4)
        outleft2, outright2 = split(out2)

        #check if the pair matches expected
        leftdiff = [0,2,2,0,0,0,0,2,2,0,2,2,1,0,2,0]
        rightdiff = [2,0,0,0,0,0,1,0,0,2,1,0,0,0,0,0]
        works = True
        for biti in range(WS):
            if leftdiff[biti] == 0 and not(get(outleft1,biti)==get(outleft2,biti)):
                works = False
            elif leftdiff[biti] == 1 and not(get(outleft1,biti)!=get(outleft2,biti)):
                works = False

        for biti in range(WS):
            if rightdiff[biti] == 0 and not(get(outright1,biti)==get(outright2,biti)):
                works = False
            elif rightdiff[biti] == 1 and not(get(outright1,biti)!=get(outright2,biti)):
                works = False

        if works:
            filtered.append(pair) #Pair has correct output

bits_to_guess = [1,15]
print(len(filtered))
d = {}
tot = 0
for guess in range(2**len(bits_to_guess)):
    d[guess] = 0
    k = [0]*WS
    for biti in range(len(bits_to_guess)):
        k[bits_to_guess[biti]] = get(guess,biti)
    k = convert(k)
    

    for pair in filtered:
        out1 = simon(pair[0],keys,rounds=4)
        outleft1, outright1 = split(out1)
        out2 = simon(pair[1],keys,rounds=4)
        outleft2, outright2 = split(out2)

        newleft1 = outright1
        newright1 = outleft1 ^ f(outright1) ^ k

        newleft2 = outright2
        newright2 = outleft2 ^ f(outright2) ^ k

        outleft1, outleft2, outright1, outright2 = newleft1, newleft2, newright1, newright2
        newleft1 = outright1
        newright1 = outleft1 ^ f(outright1) ^ 0

        newleft2 = outright2
        newright2 = outleft2 ^ f(outright2) ^ 0
        
        if enddiff[0] == newleft1 ^ newleft2 and enddiff[1] == newright1 ^ newright2:
            d[guess]+=1

print(d)
m = -1
mc = 0
for x in d.keys():
    if d[x] > mc:
        m = x
        mc = d[x]

for biti in range(len(bits_to_guess)):
    print("bit",bits_to_guess[biti],"is",get(m,biti))
print("Answer:")
for biti in range(len(bits_to_guess)):
    print("bit",bits_to_guess[biti],"is",get(keys[3],bits_to_guess[biti]))
