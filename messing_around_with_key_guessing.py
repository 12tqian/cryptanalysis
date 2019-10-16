from util import *
from random import randint

#try to break 15 rounds
#At round 0, diff is (0, d{6})
startdiff = [0,convert2([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])]

#At round 13, diff is (d{14},0)
enddiff = [convert2([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),0]
NC = 100 #Number of pair candidates

def rand_word(size = WS):
    return randint(0,2**(WS)-1)

#Generate a bunch of pair candidates
pairs = []
for count in range(NC):
    left1, right1 = rand_word(), rand_word()
    left2, right2 = left1^startdiff[0], right1^startdiff[1]
    pairs.append([compose(left1,right1),compose(left2,right2)])


print(pairs)
