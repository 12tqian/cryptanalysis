from util import *
from simon import *
from random import randint

#try to break 3 rounds
#At round 0, diff is (0, d{6})
startdiff = [0,convert2([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])]

#At round 2, diff is (d{8},d{6})
enddiff = [convert2([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]),convert2([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])]
NC = 100 #Number of pair candidates

def rand_word(size = WS):
    return randint(0,2**(WS)-1)

#Generate a bunch of pair candidates
pairs = []
for count in range(NC):
    left1, right1 = rand_word(), rand_word()
    left2, right2 = left1^startdiff[0], right1^startdiff[1]
    pairs.append([compose(left1,right1),compose(left2,right2)])


bits_to_guess = [13,15]
d = {}
for guess in range(2**len(bits_to_guess)):
    d[guess] = 0
    k = [0]*WS
    for biti in range(len(bits_to_guess)):
        k[bits_to_guess[biti]] = get(guess,biti)

    for pair in pairs:
        out1 = simon(pair[0],rounds=3)
        outleft1, outright1 = split(out1)
        out2 = simon(pair[1],rounds=3)
        outleft2, outright2 = split(out2)

        #check if the pair matches expected
        leftdiff = [2,0,0,0,0,0,1,0,0,2,1,0,0,0,0,0]
        rightdiff = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
        works = True
        for biti in range(WS):
            if leftdiff[biti] == 0 and not(get(outleft1,biti)==get(outleft2,biti)):
                works = False
            elif leftdiff[biti] == 1 and not(get(outleft1,biti)!=get(outleft2,biti)):
                works = False

        if not(works):
            break #Pair doesn't fit

        newleft1 = outright1
        newright1 = outleft1 ^ f(outright1) ^ k

        newleft2 = outright2
        newright2 = outleft2 ^ f(outright2) ^ k
        
        if enddiff[0] == newleft1 ^ newleft2 and enddiff[1] == newright1 ^ newright2:
            d[guess]+=1

print(d)
                    
                    
