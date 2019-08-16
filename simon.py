from util import *
"""
Simon cipher
"""


def key_schedule(k, m, z, r):
    size = WS * m
    keys = [(k >> (WS*(i)))&(2**WS-1) if i < m else None for i in range(r)]
    for i in range(m, r):
        tmp = rotr(keys[i-1], 3)
        if m == 4: tmp ^= keys[i-3]
        tmp ^= rotr(tmp, 1)
        keys[i] = (2**WS - 1 - keys[i-m]) ^ 3 ^ tmp ^ ((z >> ((61 - (i - m)) % 62)) & 1)
    return keys

def rf(w1,w2,key):
    """Round function"""
    return w2 ^ (rotl(w1,1) & rotl(w1,8))^ rotl(w1,2) ^ key, w1

def simon(block, keys=[], rounds=0):
    if rounds == 0:
        if not len(keys):
            keys = key_schedule(MASTER_KEY, 4, Z, ROUNDS)

        return simon(block, keys, ROUNDS)
    w1 = block >> WS
    w2 = block % (1<<WS)

    for r in range(rounds):
        w1,w2 = rf(w1,w2,keys[r])
    return w1 << WS | w2
    
    
if __name__ == "__main__":
    keys = key_schedule(0x1111222233334444, 4, Z, ROUNDS)
    print(keys)
    print(hex(simon(0x41414141, keys, 32)))
