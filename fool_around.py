from util import *
a = 1
b = 8
c = 2
def p(alpha, beta):
    vb = (rotl(alpha, a)|rotl(alpha, b))
    db = ((rotl(alpha, b)|flip(rotl(alpha, a)))|rotl(alpha, 2*a - b))
    gamma = (beta^(rotl(alpha, c)))
    if a == 2**WS - 1 and wt(gamma)%2 == 0:
        return WS - 1
    elif alpha != 2**WS - 1 and (gamma&flip(vb) == 0) and ((gamma^rotl(gamma, a-b))|db) == 0:
        return wt((vb^db))
    return -1
print(p(5, 1))
