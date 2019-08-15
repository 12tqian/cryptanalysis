WS = 16
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
    
diff = [[1, 2]]
amt = int(2**30.2)
st = [diff[0][1], (diff[0][0]&f(diff[0][1]))]
val = st[1] + (st[0]<<WS)
pairs = []
cnt = 0
for i in range(2**(2*WS)):
    pairs.append([i, (i^val)])
    cnt += 1
    if(cnt == amt):
        break
filtered = []
for x in pairs:
    e1 = simon(x[0])
    e2 = simon(x[1])
    L1 = (e1>>WS)
    R1 = (e1<<WS)
    L2 = (e2>>WS)
    R2 = (e2<<WS)
    LDiff = (R1^R2)
    RDiff = (L1^f(R1))^(L2^f(R2))
    
    
    
    
