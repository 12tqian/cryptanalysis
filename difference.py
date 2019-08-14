WS = 16
ROT = [1, 8, 2]
ROUNDS = 128
chain = [-1 for i in range(ROUNDS)]
prob = -1
def get(a, n):
    return (a>>n)&1


def rotl(n, d): 
    # rotate n by d to the left
    # In n<<d, last d bits are 0. 
    # To put first 3 bits of n at  
    # last, do bitwise or of n<<d 
    # with n >>(INT_BITS - d)  
    return (n << d)|(n >> (WS - d))
def rotation_weight(a, r):
    #returns the difference thing
    #each difference formed by 2^(n-cnt) pairs
    #therer are 2^cnt number of differences
    b = [0 for x in range(WS)]
    cnt = 0
    use = 1
    for i in range(WS):
        if((get(a, i) == 1 or get(a, (i-r)%WS) == 1)  and b[i] == 0):
            b[i] = 1
            cnt += 1
        if get(a, i) == 0 and get(a, (i-r+WS)%WS) == 1 and get(a, (i+r)%WS) == 1:
            b[i] = -use
            b[(i+r)%WS] = -use
            use+= 1
    return b, cnt
def weight(l, r):
    s1 = rotl(l, 1)
    res, cnt = rotation_weight(s1, ROT[1] - ROT[0])
    s2 = rotl(l, 2)
    fin = [0 for x in range(WS)]
    for i in range(WS):
        if res[i] >= 0:
            fin[i] = (res[i]^get(s2, i))
        else:
            fin[i] = res[i]
    return fin, cnt
def threshold_reached(level, probability):
    if(probability/(level+1) <=  5):
        return False
    return True

time = 0
def convert(a):
    ret = 0
    for i in range(WS):
            ret += (2**i)*a[i]
    return ret
def dfs(l, r, tot, depth):
    global time
    time += 1
    global prob
    prob = tot
    if(depth != ROUNDS and threshold_reached(depth, tot)):
      #  print(depth, tot)
        return False
    if(depth == ROUNDS and threshold_reached(depth, tot)):
        #print(chain)
       # print(depth, tot)
        return False
    if(depth == ROUNDS):
       return True
    nxt, num = weight(l, r)
   # print(num, "AASDA")
    #print(l, r)
    for mask in range(0, 2**num):
        cur = 0
        in_use = [-1 for x in range(WS+1)]
        use = [0 for x in range(WS)]
        for i in range(WS):
            if(nxt[i] == 0):
                use[i] = nxt[i]
            elif nxt[i] == 1:
                use[i] = get(mask, cur)
                cur += 1
            else:
                if(in_use[-nxt[i]] == -1):
                    in_use[-nxt[i]] = get(mask, cur)
                    cur+= 1
                    use[i] = in_use[-nxt[i]]
                else:
                    use[i] = in_use[-nxt[i]]
        print(nxt)
       # print(use)
        if(convert(use) ==0):
            continue
        translate = convert(use)
        chain[depth] = translate
        #print(l, r, translate, l, mask)
        if(dfs(translate, l, tot + num, depth+ 1)):
            return True
        chain[depth] = -1
    return False


    
    
dfs(542, 112, 0, 0)
print(chain)
print(prob)


