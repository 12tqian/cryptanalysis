from util import *
def p(alpha, beta=getBeta(alpha)):
    vb = (rotl(alpha, ROT[0])|rotl(alpha, ROT[1]))
    db = ((rotl(alpha, ROT[1])&flip(rotl(alpha, ROT[0])))&rotl(alpha, 2*ROT[0] - ROT[1]))
    gamma = (beta^(rotl(alpha, ROT[2])))
    if alpha == 2**WS - 1 and wt(gamma)%2 == 0:
        return WS - 1
    elif alpha != 2**WS - 1 and (gamma&flip(vb) == 0) and ((gamma^rotl(gamma, ROT[0] - ROT[1]))&db) == 0:
        return wt((vb^db))
    return -1
def getBeta(alpha):
    v1 = 0
    v2 = alpha
    e1 = (f(v1))
    e2 = (f(v2))
    return (e1^e2)


ROUNDS = 5
