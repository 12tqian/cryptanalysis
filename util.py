WS = 16
ROT = [1, 8, 2]
ROUNDS = 128
def rotl(n, d): 
    # rotate n by d to the left
    # In n<<d, last d bits are 0. 
    # To put first 3 bits of n at  
    # last, do bitwise or of n<<d 
    # with n >>(INT_BITS - d)  
    return (n << d)|(n >> (WS - d))

def rotr(n, d):
    return (n >> d)|(n << (WS - d)); 
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
