#Used for debugging. Now obsolete.
from util import *
from simon import *
from random import randint


def rand_word(size = WS):
    return randint(0,2**(WS)-1)

def backtrack(left1,right1,left2,right2,k):
    newleft1 = right1
    newright1 = left1 ^ f(right1) ^ k
    
    newleft2 = right2
    newright2 = left2 ^ f(right2) ^ k
    return newleft1, newright1, newleft2, newright2

#try to break 5 rounds
#At round 0, diff is (0, d{6})
startdiff = [0,convert2([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])]

#At round 2, diff is (d{8},d{6})
enddiff = [convert2([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]),convert2([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])]

leftdiff = [2,0,2,2,2,0,2,0,2,2,2,2,2,2,1,2]#[0,2,2,0,0,0,0,2,2,0,2,2,1,0,2,0] #At round rounds, diff is this
rightdiff = [0,2,2,0,0,0,0,2,2,0,2,2,1,0,2,0]#[2,0,0,0,0,0,1,0,0,2,1,0,0,0,0,0]

NC = 1000 #Number of pair candidates
rounds = 5
extra_rounds = 3


keys = [12570, 33730, 38026, 48474, 63835]#[rand_word() for x in range(rounds)]
print("keys",keys)

#Generate a bunch of pair candidates and filter them
filtered = []
e = {}
wg = 0
wb = 0
badlist = []
for count in range(NC):
    left1, right1 = rand_word(), rand_word()
    left2, right2 = left1^startdiff[0], right1^startdiff[1]
    pair = [compose(left1,right1),compose(left2,right2)]

    out1 = simon(pair[0],keys,rounds)
    outleft1, outright1 = split(out1)
    out2 = simon(pair[1],keys,rounds)
    outleft2, outright2 = split(out2)

    #check if the pair matches expected
    works = True
    for biti in range(WS):
        if leftdiff[biti] == 0 and not(get(outleft1,biti)==get(outleft2,biti)):
            works = False
        elif leftdiff[biti] == 1 and not(get(outleft1,biti)!=get(outleft2,biti)):
            works = False
        if rightdiff[biti] == 0 and not(get(outright1,biti)==get(outright2,biti)):
            works = False
        elif rightdiff[biti] == 1 and not(get(outright1,biti)!=get(outright2,biti)):
            works = False

    #check if the pair followed the trail
    out1 = simon(pair[0],keys,2)
    outleft1, outright1 = split(out1)
    out2 = simon(pair[1],keys,2)
    outleft2, outright2 = split(out2)

    works2 = enddiff[0] == outleft1 ^ outleft2 and enddiff[1] == outright1 ^ outright2
            
    if works:
        
        e[str(pair)] = 0
        if works2:
            wg+=1
            filtered.append(pair) #Pair has correct output #Move back to always
        else:
            wb+=1
            badlist.append([outleft1 ^ outleft2,outright1 ^ outright2])
        

bits_to_guess = [[],[1,15],[0,1,2,3,7,9,13,15]] #Should have a length of extra_rounds
print("filtered",len(filtered))
d = {}

tot = 0

for kguesses in [[0, 32770, 40971],[0, 2, 40971]]:
    
    index = 0
    d[str(kguesses)] = 0

    for pair in filtered:
        out1 = simon(pair[0],keys,rounds)
        left1, right1 = split(out1)
        out2 = simon(pair[1],keys,rounds)
        left2, right2 = split(out2)

        for k in kguesses[::-1]:
            left1,right1,left2,right2 = backtrack(left1,right1,left2,right2,k)
        
        if enddiff[0] == left1 ^ left2 and enddiff[1] == right1 ^ right2:
            d[str(kguesses)]+=1
            e[str(pair)] += 1 if kguesses[1]==2 else 2
        else:
            print(pair,kguesses)
            input()
            
m = -1
mc = 0
for x in d.keys():
    if d[x] > mc:
        m = x
        mc = d[x]
m = [int(x) for x in m[1:-1].split(", ")]
print("Believes that: ")
for r in range(extra_rounds):
    ri = rounds-extra_rounds+r#Adjusted
    for biti in range(len(bits_to_guess[r])):
        print("Round",ri,"bit",bits_to_guess[r][biti],"is",get(m[r],bits_to_guess[r][biti]))
print("Answer: ")
for r in range(extra_rounds):
    ri = rounds-extra_rounds+r
    for biti in range(len(bits_to_guess[r])):
        print("Round",ri,"bit",bits_to_guess[r][biti],"is",get(keys[ri],bits_to_guess[r][biti]))
