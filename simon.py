"""
Simon cipher
"""
WS = 16 #Word size

#Rotate right
def ror(n, rotations=1, width=WS):
    """Return a given number of bitwise right rotations of an integer n,
       for a given bit field width.
    """
    rotations %= width
    if rotations < 1:
        return n
    return (n >> rotations) | ((n << (width - rotations))%(1 << width))

#Rotate left
def rol(n, rotations=1, width=WS):
    """Return a given number of bitwise left rotations of an integer n,
       for a given bit field width.
    """
    rotations %= width
    if rotations < 1:
        return n
    return ((n << rotations)%(1 << width)) | (n >> (width - rotations))

def key_schedule(k, m, z, r):
    c = 2**WS - 4
    size = WS * m
    keys = [(k >> (WS*(i)))&(2**WS-1) if i < m else None for i in range(r)]
    for i in range(m, r):
        tmp = ror(keys[i-1], 3)
        if m == 4: tmp ^= keys[i-3]
        tmp ^= ror(tmp, 1)
        keys[i] = (2**WS - 1 - keys[i-m]) ^ 3 ^ tmp ^ ((z >> ((61 - (i - m)) % 62)) & 1)
    return keys

def rf(w1,w2,key):
    """Round function"""
    return w2 ^ (rol(w1,1) & rol(w1,8))^ rol(w1,2) ^ key, w1

def simon(block, keys, rounds):
    w1 = block >> WS
    w2 = block % (1<<WS)

    for r in range(rounds):
        w1,w2 = rf(w1,w2,keys[r])

    return w1 << WS | w2

keys = key_schedule(0x1111222233334444, 4, 0b11111010001001010110000111001101111101000100101011000011100110, 32)
print(hex(simon(0x41414141, keys, 32)))
