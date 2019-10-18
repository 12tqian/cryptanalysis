from util import *
MX = 16
def g(x):
    val = x|(rotl(x, 7, MX)&flip(rotr(x, 7, MX), MX))
    return wt(val)
bad = []
for i in range(MX+1):
    bad.append(0)
for i in range((1<<MX)):
    w = wt(i)
    if( w == MX):
        continue
    if(1<= w < float(MX)/2):
        if(w + 1 == g(i)):
          #  print("a", i, bin(w))
            bad[w] = 1
    elif(float(MX)/2<= w  and w<MX):
        if(w == g(i)):
           # print("b", i, bin(w))
            bad[w] = 1
  
for i in range(1, MX):
    if bad[i] == 0:
        print(i)
print(g(21845))
