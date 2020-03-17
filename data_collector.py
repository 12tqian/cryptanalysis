from final_key_guessing import *
from time import time

trail_start_diff = [convert([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),convert([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])]
trail_ends = {5:[convert([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]),convert([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])],
              6:[convert([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]),convert([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])],
              7:[convert([0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0]),convert([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])],
              8:[convert([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]),convert([0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0])],
              9:[convert([0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0]),convert([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])],
              10:[convert([1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]),convert([0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0])],
                17:[convert([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),convert([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])]}
                
################ The code in this block determines which cipher it breaks.
##rounds = 6 #Total rounds
##extra_rounds = 3#Rounds you backtrack
##
###At round 1
##trail_start_diff = [convert([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),convert([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])]   #Put in standard form
##
###At round (rounds-extra_rounds)
##trail_end_diff = [convert([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]),convert([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])]
################

################## The code in this block determines which cipher it breaks.
##rounds = 8 #Total rounds
##extra_rounds = 3#Rounds you backtrack
##
###At round 1
##trail_start_diff = [convert([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),convert([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])]   #Put in standard form
##
###At round (rounds-extra_rounds)
##trail_end_diff = [convert([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]),convert([0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0])]
################

################## The code in this block determines which cipher it breaks.
##rounds = 17 #Total rounds
##extra_rounds = 3#Rounds you backtrack
####
#####At round 1
##trail_start_diff = [convert([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),convert([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])]   #Put in standard form
####
#####At round (rounds-extra_rounds)
##trail_end_diff = [convert([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]),convert([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])]
##################

################## The code in this block determines which cipher it breaks.
###WS = 24
##rounds = 12 #Total rounds
##extra_rounds = 3#Rounds you backtrack
##
###At round 1
##trail_start_diff = [convert([x in [8,16] for x in range(WS)]),convert([x in [6,14,18] for x in range(WS)])]   #Put in standard form
##
###At round (rounds-extra_rounds)
##trail_end_diff = [convert([x in [8] for x in range(WS)]),convert([x in [6] for x in range(WS)])]
##################

"""
for rounds in range(5,11):
    tstart = time()
    print(rounds, "rounds.")
    diff_crypt(rounds, 3, trail_start_diff, trail_ends[rounds])
    print(time()-tstart, "seconds for", rounds, "rounds.")
"""

trials = 100
for NC in range(2,40,2):
    tot = 0
    for x in range(trials):
        tot += diff_crypt(5, 2, trail_start_diff, trail_ends[6], NC, False)
    print(NC,"\t",tot/trials)
