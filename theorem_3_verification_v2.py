from util import *
st = []
MX = 16

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



def thm3(alpha):
    w = wt(alpha)
    if 1<=w and w<MX/2:
        return w+1
    elif w<MX:
        return w
    else:
        return MX-1

for i in range((1<<MX)):
    w = wt(i)
    print(thm3(i),prob(i),w)