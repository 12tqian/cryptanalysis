
ws = 16
lac = [[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]    #left  bits
rac = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
kib = []    #Which bits in the keys are important
rounds = 4  #How many rounds do you trace
sr = 14 #start round (for display purposes)

#0 is inactive
#1 is active
#2 is unknown

for r in range(rounds):
    kib.append([0 for x in range(ws)])
    for b in range(ws):
        if(rac[-1][b] > 0):
            kib[-1][(b+7)%ws] = 1
            kib[-1][(b-7)%ws] = 1
    rac.append(lac[-1][:])
    lac.append(rac[-2][:])
    for b in range(ws):
        if rac[-1][b] == 1:
            lac[-1][(b-1)%ws] = 2
            lac[-1][(b-8)%ws] = 2
            if lac[-1][(b-2)%ws] == 0:
                lac[-1][(b-2)%ws] = 1
            else:
                lac[-1][(b-2)%ws] = 2
        elif rac[-1][b] == 2:
            lac[-1][(b-1)%ws] = 2
            lac[-1][(b-8)%ws] = 2
            lac[-1][(b-2)%ws] = 2
            
#Display
curr = sr
print("LR", curr, ":", "".join([str(x) for x in lac[0]]), end="     ")
print("".join([str(x) for x in rac[0]]))
for r in range(rounds):
    print("\t\t\t\t\t\t", "".join([str(x) for x in kib[r]]), "K", curr)
    curr += 1
    print("LR", curr, ":", "".join([str(x) for x in lac[r+1]]), end="     ")
    print("".join([str(x) for x in rac[r+1]]))