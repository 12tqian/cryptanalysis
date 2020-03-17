from util import *
from simon import *
from truncated_trail import *
from random import randint
import time


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


def diff_crypt(rounds, extra_rounds, trail_start_diff, trail_end_diff, num_pairs=100, disp=True):
    slr_diff = [[],[]]  #Differential (with 0's, 1's, 2's) expected at round (round-1) AKA second to last round. Compared with last round inverted.
    slr_diff[0], slr_diff[1], bits_to_guess = trail_info(trail_end_diff, extra_rounds, rounds-extra_rounds)
    #bits_to_guess: Should have a length of extra_rounds, first list should be empty

    NC = num_pairs #Number of pair candidates
    gonethrough = 0

    keys = [rand_word() for x in range(rounds)]
    if disp:
        print("keys",keys)

    #Generate a bunch of pair candidates and filter them
    filtered = []
    while len(filtered) < NC:
        gonethrough+=1
        left1, right1 = rand_word(), rand_word()
        left2, right2 = left1^trail_start_diff[1], right1^f(left1^trail_start_diff[1])^f(left1)^trail_start_diff[0] #modified to extract an extra round.
        pair = [compose(left1,right1),compose(left2,right2)]

        out1 = simon(pair[0],keys,rounds)
        outleft1, outright1 = split(out1)
        out2 = simon(pair[1],keys,rounds)
        outleft2, outright2 = split(out2)

        #Invert last round
        slrdiffleft = (outright1^outright2) #Second to last round diff
        slrdiffright = (outleft1^f(outright1))^(outleft2^f(outright2))


        #check if the pair matches expected after rounds rounds
        if color_match(slrdiffleft,slr_diff[0]) and color_match(slrdiffright,slr_diff[1]):
            filtered.append(pair) #Pair has correct output

    if disp:
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
    if disp:
        print("Believes that: ")
    for r in range(extra_rounds):
        ri = rounds-extra_rounds+r#Adjusted
        for biti in range(len(bits_to_guess[r])):
            if disp:
                print("Round",ri,"bit",bits_to_guess[r][biti],"is",get(m[r],bits_to_guess[r][biti]))
            belief += str(get(m[r],bits_to_guess[r][biti]))

    #print answer
    answer = ""

    if disp:
        print("Answer: ")
    for r in range(extra_rounds):
        ri = rounds-extra_rounds+r
        for biti in range(len(bits_to_guess[r])):

            if disp:
                print("Round",ri,"bit",bits_to_guess[r][biti],"is",get(keys[ri],bits_to_guess[r][biti]))
            answer += str(get(keys[ri],bits_to_guess[r][biti]))

    #Find runner up
    mc = 0
    m_runnerup = -1
    for x in d.keys():
        if d[x] > mc and x != str(m):
            m_runnerup = x
            mc = d[x]

    if disp:
        print("Winner:",m,d[str(m)])
        print("Runner up:", m_runnerup, d[m_runnerup])
    

        print(answer==belief)   #Did it work?
    return answer==belief
