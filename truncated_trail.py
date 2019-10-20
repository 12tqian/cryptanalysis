from util import *

def trail_info(diff, extra_rounds, sr=0, disp=False):
    """diff is of the form [binint,binint], it is the end of the trail."""
    lac = [arr(diff[0])] #Standard form
    rac = [arr(diff[1])]
    kib = []    #Which bits in the keys are important

    #0 is inactive
    #1 is active
    #2 is unknown

    for r in range(extra_rounds):
        kib.append([0 for x in range(WS)])
        for b in range(WS):
            if(rac[-1][b] > 0 and r>0):
                kib[-1][(b+7)%WS] = 1
                kib[-1][(b-7)%WS] = 1
        rac.append(lac[-1][:])
        lac.append(rac[-2][:])  #Swaps left and right
        for b in range(WS):
            if rac[-1][b] == 1:
                lac[-1][(b+1)%WS] = 2
                lac[-1][(b+8)%WS] = 2
                if lac[-1][(b+2)%WS] == 0:
                    lac[-1][(b+2)%WS] = 1
                else:
                    lac[-1][(b+2)%WS] = 2
            elif rac[-1][b] == 2:
                lac[-1][(b+1)%WS] = 2
                lac[-1][(b+8)%WS] = 2
                lac[-1][(b+2)%WS] = 2
                
                
    #Display in readable form (15 14 ... 0), the way it appears in paper
    if(disp):
        curr = sr
        print("LR", curr, ":", "".join([str(x) for x in lac[0]])[::-1], end="     ")
        print("".join([str(x) for x in rac[0]])[::-1])
        for r in range(extra_rounds):
            print("\t\t\t\t\t\t", "".join([str(x) for x in kib[r]])[::-1], "K", curr)
            curr += 1
            print("LR", curr, ":", "".join([str(x) for x in lac[r+1]])[::-1], end="     ")
            print("".join([str(x) for x in rac[r+1]])[::-1])

    bits_to_guess = []
    for key in kib:
        bits_to_guess.append([])
        for b in range(WS):
            if key[b] == 1:
                bits_to_guess[-1].append(b)
    return lac[-2], rac[-2], bits_to_guess

if __name__ == "__main__":
    diff = [convert([x in [8] for x in range(WS)]),convert([x in [6] for x in range(WS)])]
    trail_info(diff, 3, 9, True)
