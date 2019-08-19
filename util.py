WS = 16
Z = 0b11111010001001010110000111001101111101000100101011000011100110
ROT = [8, 1, 2]
ROUNDS = 32

MASTER_KEY = 0x1111222233334444

def rotl(n, d, SZ = WS):
    d %= SZ
    if(d<0):
        d += SZ
    return ((n << d)%(1 << SZ)) | (n >> (SZ - d))

def rotr(n, d, SZ = WS):
    d %= SZ
    if(d<0):
        d+= SZ
    return (n >> d)|((n << (SZ - d))%(1<<SZ))

def f(x):
    return ((rotl(x, 1)&rotl(x, 8))^rotl(x, 2))
def get(a, n):
    return (a>>n)&1
def convert(a, SZ = WS):
    ret = 0
    for i in range(SZ):
            ret += (2**i)*a[i]
    return ret
def arr(a, SZ = WS):
    ret = []
    for i in range(SZ):
            ret.append(get(a, i))
    return ret
def compose(l, r, SZ = WS):
    return r + (l<<SZ)
def split(x, SZ = WS):
    return (x>>SZ), ((x)%(1<<SZ))
def flip(x, SZ = WS):
    return (1<<SZ) - 1 - x
def wt(x):
    return bin(x).count("1")
