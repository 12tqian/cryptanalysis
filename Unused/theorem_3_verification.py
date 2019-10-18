from util import *
st = []
MX = 6
"""def p(alpha, beta):
    print(MX)
    vb = (rotl(alpha, ROT[0], MX)|rotl(alpha, ROT[1], MX))
    db = ((rotl(alpha, ROT[1], MX)&flip(rotl(alpha, ROT[0], MX), MX))&rotl(alpha, 2*ROT[0] - ROT[1], MX))
    gamma = (beta^(rotl(alpha, ROT[2], MX)))
    if alpha == 2**MX - 1 and wt(gamma)%2 == 0:
        return MX - 1
    elif alpha != 2**MX - 1 and (gamma&flip(vb, MX) == 0) and ((gamma^rotl(gamma, ROT[0] - ROT[1]))&db, MX) == 0:
        return wt((vb^db))
    return -1"""
def p(alpha, beta):
    vb = (rotl(alpha, ROT[0], MX)|rotl(alpha, ROT[1], MX))
    db = ((rotl(alpha, ROT[1], MX)&flip(rotl(alpha, ROT[0], MX), MX))&rotl(alpha, 2*ROT[0] - ROT[1], MX))
    gamma = (beta^(rotl(alpha, ROT[2], MX)))
    if alpha == 2**MX - 1 and wt(gamma)%2 == 0:
        return MX - 1
    elif alpha != 2**MX - 1 and ((gamma&flip(vb, MX)) == 0) and ((gamma^rotl(gamma, ROT[0] - ROT[1], MX))&db) == 0:
        return wt((vb^db))
    return -1
def getBeta(alpha):
    v1 = 0
    v2 = alpha
    e1 = (f(v1, MX))
    e2 = (f(v2, MX))
    return (e1^e2)
def prob(alpha):
    return p(alpha, getBeta(alpha))


for i in range(MX+1):
    st.append([])

for i in range((1<<MX)):
    w = wt(i)
    if(prob(i) == -1):
        print(i)
    st[w].append(prob(i))
for i in range(len(st)):
    st[i].sort()
print(st)
