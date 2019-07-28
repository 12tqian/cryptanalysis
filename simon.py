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

def rf(w1,w2,key):
    """Round function"""
    return w2 ^ (rol(w1,1) & rol(w1,8))^ rol(w1,2) ^ key, w1

def simon(block, keys, rounds):
    w1 = block >> WS
    w2 = block % (1<<WS)

    for r in range(rounds):
        w1,w2 = rf(w1,w2,keys[r])

    return w1 << WS | w2
