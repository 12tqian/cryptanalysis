from util import*
from random import random
#Nondeterministic (not optimal)

def getBeta(alpha):
    v1 = 0
    v2 = alpha
    e1 = (f(v1))
    e2 = (f(v2))
    return (e1^e2)
def p(alpha, beta=-1):
    if(beta==-1):
        beta = getBeta(alpha)
    vb = (rotl(alpha, ROT[0])|rotl(alpha, ROT[1]))
    db = ((rotl(alpha, ROT[1])&flip(rotl(alpha, ROT[0])))&rotl(alpha, 2*ROT[0] - ROT[1]))
    gamma = (beta^(rotl(alpha, ROT[2])))
    if alpha == 2**WS - 1 and wt(gamma)%2 == 0:
        return WS - 1
    elif alpha != 2**WS - 1 and (gamma&flip(vb) == 0) and ((gamma^rotl(gamma, ROT[0] - ROT[1]))&db) == 0:
        return wt((vb^db))
    return -1


def getRandom(prob=.1):
    """Gets random string of length WS with a relatively low hamming weight, according to prob"""
    return convert([random() < prob for x in range(WS)])

class Trail:
    def __init__(self,left,right):
        """if the trail is [a,b,c,d,e] this represents
        a b
        b c
        c d
        d e"""
        self.trail = [left,right]
        self.prob = 0
    def newprob(self,newdiff):
        return self.prob + p(self.trail[-2],newdiff)
    def add(self, newdiff):
        self.prob = newprob(newdiff)
        self.trail.append(newdiff)
        
ROUNDS = 5
