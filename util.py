WS = 16
Z = 0b11111010001001010110000111001101111101000100101011000011100110
ROT = [1, 8, 2]
ROUNDS = 32
def rotl(n, d): 
    return ((n << d)%(1 << WS)) | (n >> (WS - d))

def rotr(n, d):
    return (n >> d)|((n << (WS - d))%(1<<WS))

def f(x):
    return ((rotl(x, 1)&rotl(x, 8))^rotl(x, 2))
def get(a, n):
    return (a>>n)&1
def convert(a):
    ret = 0
    for i in range(WS):
            ret += (2**i)*a[i]
    return ret
def arr(a):
    ret = []
    for i in range(WS):
            ret.append(get(a, i))
    return ret
def compose(l, r):
    return r + (l<<WS)
def split(x):
    return (x>>WS), ((x<<WS)%(1<<WS))
