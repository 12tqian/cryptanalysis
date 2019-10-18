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

#try to break 6 rounds
#At round 1, diff is (0, d{6})
startdiff = [0,convert2([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])]

#At round 3, diff is (d{8},d{6})
enddiff = [convert2([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]),convert2([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])]

leftdiff = [2,0,2,2,2,0,2,0,2,2,2,2,2,2,1,2]#[0,2,2,0,0,0,0,2,2,0,2,2,1,0,2,0] #At round rounds, diff is this
rightdiff = [0,2,2,0,0,0,0,2,2,0,2,2,1,0,2,0]#[2,0,0,0,0,0,1,0,0,2,1,0,0,0,0,0]

NC = 100 #Number of pair candidates
rounds = 6
extra_rounds = 3


keys = [rand_word() for x in range(rounds)]
print("keys",keys)

#Generate a bunch of pair candidates and filter them
filtered = []
for count in range(NC):
    left1, right1 = rand_word(), rand_word()
    left2, right2 = left1^startdiff[1], right1^f(left1^startdiff[1])^f(left1)^startdiff[0] #modified to extract an extra round.
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

    if works:
        filtered.append(pair) #Pair has correct output

bits_to_guess = [[],[1,15],[0,1,2,3,7,9,13,15]] #Should have a length of extra_rounds
print("filtered",len(filtered))
d = {}
tot = 0
for guess in range(2**sum(len(bits_to_guess[r]) for r in range(extra_rounds))):
    
    kguesses = []   #In order of increasing round numbers
    krguesses=[] #kguesses, but random bits in unimportant slots
    index = 0
    for r in range(extra_rounds):
        kr = [randint(0,1) for x in range(WS)]
        k = [0]*WS
        for biti in range(len(bits_to_guess[r])):
            k[bits_to_guess[r][biti]] = get(guess,index)
            kr[bits_to_guess[r][biti]] = get(guess,index)
            index+=1
        k = convert(k)
        kr = convert(kr)
        kguesses.append(k)
        krguesses.append(kr)
    d[str(kguesses)] = 0

    for pair in filtered:
        out1 = simon(pair[0],keys,rounds)
        left1, right1 = split(out1)
        out2 = simon(pair[1],keys,rounds)
        left2, right2 = split(out2)

        for k in krguesses[::-1]:
            left1,right1,left2,right2 = backtrack(left1,right1,left2,right2,k)
        
        if enddiff[0] == left1 ^ left2 and enddiff[1] == right1 ^ right2:
            d[str(kguesses)]+=1

#print("d",d)
m = -1
mc = 0
for x in d.keys():
    if d[x] > mc:
        m = x
        mc = d[x]
m = [int(x) for x in m[1:-1].split(", ")]
belief = ""
print("Believes that: ")
for r in range(extra_rounds):
    ri = rounds-extra_rounds+r#Adjusted
    for biti in range(len(bits_to_guess[r])):
        print("Round",ri,"bit",bits_to_guess[r][biti],"is",get(m[r],bits_to_guess[r][biti]))
        belief += str(get(m[r],bits_to_guess[r][biti]))
answer = ""
print("Answer: ")
for r in range(extra_rounds):
    ri = rounds-extra_rounds+r
    for biti in range(len(bits_to_guess[r])):
        print("Round",ri,"bit",bits_to_guess[r][biti],"is",get(keys[ri],bits_to_guess[r][biti]))
        answer += str(get(keys[ri],bits_to_guess[r][biti]))
print(answer==belief)
