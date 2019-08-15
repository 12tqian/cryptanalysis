from util import *
from keys import *
from simon import *


def transform(x, mask, length, key):
    cnt = 0
    for i in range(WS):
        if(key[i] == 2):
            x += (get(mask, cnt)<<i)
            cnt+= 1
    return x

def verify(key_list):
    full = crack(Z, ROUNDS, key_list[0], key_list[1], key_list[2], key_list[3])
    for case in test:
        encrypted = simon(case[0], full, ROUNDS)
        if encrypted != case[1]:
            return False
    return True
        
def brute_force(candidates):
    for candidate in candidates:
        num = []
        lengths = []
        cnt = 0
        for i in candidate:
            lengths.append(0)
            val = 0
            for j in range(WS):
                if(i[j] == 2):
                    lengths[cnt] += 1
                else:
                    val += i[j]*(1<<j)
            num.append(val)
            cnt += 1

        #Check all possibilities
        for mask in range(2**sum(lengths)):
            masks = []

            #Splice out the correct bits from mask
            for r in range(len(lengths)):
                masks.append(mask%(2**length[r]))
                mask = mask >> length[r]

            key_list = []
            for i in range(len(lengths)):
                key_list.append(transform(num[i], masks[i], lengths[i], candidate[i]))
            if(verify(key_list)):
                return key_list
        return []
                        
        
                
