import random
from util import *
from simon import *

def f(x):
    return ((rotl(x, 1)&rotl(x, 8))^rotl(x, 2))

def gen_pairs(start, end, amt):
    """Generates amt pairs that have diff of start after the first round, diff of end after second to last round"""
    lstart, rstart = split(start)

    final_pairs = []
    cnt = 0
    while cnt < amt:
        L_x = random.randint(0,2**WS)
        R_x = random.randint(0,2**WS)
        pair = [compose(L_x, R_x), compose(L_x^rstart, R_x^f(L_x^rstart)^f(L_x)^lstart)]

        lend1, rend1 = split(simon(pair[0]))
        lend2, rend2 = split(simon(pair[1]))
        
        #Invert last round
        LDiff = (rend1^rend2)
        RDiff = (lend1^f(rend1))^(lend2^f(rend2))

        #Keep only pairs that have correct ending
        if compose(LDiff, RDiff) == end:
            final_pairs.append(pair)
            cnt += 1

    return final_pairs

if __name__ == "__main__":
    print(gen_pairs(0x1234, 0x8765, 1))
