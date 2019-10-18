from util import *
from simon import *
from truncated_trail import *
from random import randint


def rand_word(size = WS):
    return randint(0,2**(WS)-1)

def backtrack(left1,right1,left2,right2,k):
    newleft1 = right1
    newright1 = left1 ^ f(right1) ^ k
    
    newleft2 = right2
    newright2 = left2 ^ f(right2) ^ k
    return newleft1, newright1, newleft2, newright2

def color_match(diff, expected):
    for biti in range(WS):
        if expected[biti] in [0,1] and expected[biti] != get(diff,biti):
            return False
    return True

################ The code in this block determines which cipher it breaks.
rounds = 8 #Total rounds    #Dependent
extra_rounds = 3#Dependent

#try to break 8 rounds
#At round 1, diff is (0, d{6})
trail_start_diff = [convert([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),convert([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])]   #Dependent

#At round 5, diff is (d{12},d{6,10})
trail_end_diff = [convert([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]),convert([0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0])] #Dependent
################

end_diff = [[],[]]
end_diff[0], end_diff[1], bits_to_guess = trail_info(trail_end_diff, extra_rounds, rounds-extra_rounds)
#bits_to_guess: Should have a length of extra_rounds, first list should be empty

NC = 100 #Number of pair candidates

keys = [rand_word() for x in range(rounds)]
print("keys",keys)

#Generate a bunch of pair candidates and filter them
filtered = []
while len(filtered) < NC:
    left1, right1 = rand_word(), rand_word()
    left2, right2 = left1^trail_start_diff[1], right1^f(left1^trail_start_diff[1])^f(left1)^trail_start_diff[0] #modified to extract an extra round.
    pair = [compose(left1,right1),compose(left2,right2)]

    out1 = simon(pair[0],keys,rounds)
    outleft1, outright1 = split(out1)
    out2 = simon(pair[1],keys,rounds)
    outleft2, outright2 = split(out2)

    #check if the pair matches expected after rounds rounds
    if color_match(outleft1^outleft2,end_diff[0]) and color_match(outright1^outright2,end_diff[1]):
        filtered.append(pair) #Pair has correct output

print("filtered",len(filtered))
d = {}  #Maps key guesses to number of correct matches
for guess in range(2**sum(len(bits_to_guess[r]) for r in range(extra_rounds))): #Iterates through all configurations of important bits
    
    kguesses = []   #In order of increasing round numbers. Used soley as a key in map. Elements are integers
    krguesses=[] #kguesses, but random bits in unimportant slots. Used in the actual backtracking. Elements are lists of bits
    index = 0 #Index of bit in guess we are currently using
    for r in range(extra_rounds):
        kr = [randint(0,1) for x in range(WS)]  #Randomness
        k = [0]*WS
        for biti in range(len(bits_to_guess[r])):
            k[bits_to_guess[r][biti]] = get(guess,index)
            kr[bits_to_guess[r][biti]] = get(guess,index)
            index+=1
        k = convert(k)
        kguesses.append(k)
        krguesses.append(kr)
    d[str(kguesses)] = 0

    for pair in filtered:
        
        for r in range(extra_rounds):
            for biti in range(WS):
                if biti not in bits_to_guess[r]:
                    krguesses[r][biti] = randint(0,1)   #Redo the randomness for unimportant key bits
        

        #Get final output from oracle
        out1 = simon(pair[0],keys,rounds)   
        left1, right1 = split(out1)
        out2 = simon(pair[1],keys,rounds)
        left2, right2 = split(out2)

        #Backtrack to end of trail
        for k in krguesses[::-1]:
            left1,right1,left2,right2 = backtrack(left1,right1,left2,right2,convert(k))

        #See if it's a correct match
        if trail_end_diff[0] == left1 ^ left2 and trail_end_diff[1] == right1 ^ right2:
            d[str(kguesses)]+=1

#Find largest dictionary element
m = -1
mc = 0
for x in d.keys():
    if d[x] > mc:
        m = x
        mc = d[x]
m = [int(x) for x in m[1:-1].split(", ")]

#print result
belief = ""
print("Believes that: ")
for r in range(extra_rounds):
    ri = rounds-extra_rounds+r#Adjusted
    for biti in range(len(bits_to_guess[r])):
        print("Round",ri,"bit",bits_to_guess[r][biti],"is",get(m[r],bits_to_guess[r][biti]))
        belief += str(get(m[r],bits_to_guess[r][biti]))

#print answer
answer = ""
print("Answer: ")
for r in range(extra_rounds):
    ri = rounds-extra_rounds+r
    for biti in range(len(bits_to_guess[r])):
        print("Round",ri,"bit",bits_to_guess[r][biti],"is",get(keys[ri],bits_to_guess[r][biti]))
        answer += str(get(keys[ri],bits_to_guess[r][biti]))
        
print(answer==belief)   #Did it work?

#Find runner up
mc = 0
m_runnerup = -1
for x in d.keys():
    if d[x] > mc and x != str(m):
        m_runnerup = x
        mc = d[x]
print("Winner:",m,d[str(m)])
print("Runner up:", m_runnerup, d[m_runnerup])
