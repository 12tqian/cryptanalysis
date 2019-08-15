WS = 16
import random
from util import *
from simon import *

def f(x):
    return ((rotl(x, 1)&rotl(x, 8))^rotl(x, 2))

def gen_pairs(start, end, amt):
    """Generates amt pairs that have diff of start after the first round, diff of end after second to last round"""
    lstart = start >> WS
    rstart = start % (1<<WS)

    pairs = []
    for i in range(amt):
        L_x = random.randint(0,2**WS)
        R_x = random.randint(0,2**WS)
        pairs.append([compose(L_x, R_x), compose(L_x^rstart, R_x^f(R_x)^lstart)])

    print(pairs)
    #Keep only pairs that have correct ending
    final_pairs = []
    for x in pairs:
        lend1, rend1 = split(simon(x[0]))
        lend2, rend2 = split(simon(x[1]))        

        #Invert last round
        LDiff = (rend1^rend2)
        RDiff = (lend1^f(rend1))^(lend2^f(rend2))

        if compose(LDiff, RDiff) == desired:
            final_pairs.append(x)

    return final_pairs

if __name__ == "__main__":
    print(gen_pairs(0x12345678, 0x87654321, 10))
