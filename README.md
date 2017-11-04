# randomFool
import numpy as np
import random as rand
sq = 16
darts = 8
criterion = 3
gt2 = gt3 = gt4 = gt1 = gt5 = gt6= gt7= 0
trials =1000000
bintots = np.zeros([sq])
for jj in range(trials):
    bins = np.zeros([sq])
    for kk in range(darts):
        posi = rand.random() * sq
        bintots[int(posi)] +=1
        bins[int(posi)] +=1
    for hh in range(darts):
        if bins[hh] > 7:
            gt7 +=1
        elif bins[hh] > 6:
            gt6 +=1
        elif bins[hh] > 5:
            gt5 +=1
        if bins[hh] > 4:
            gt4 +=1
        elif bins[hh] > 3:
            gt3 +=1
        elif bins[hh] > 2:
            gt2 +=1
        elif bins[hh] > 1:
            gt1 +=1

print(bintots)
print('gt1:' + str(gt1) + ' > ' + str(100.0*gt1/trials) + '%')
print('gt2:' + str(gt2) + ' > ' + str(100.0*gt2/trials) + '%')
print('gt3:' + str(gt3)+ ' > ' + str(100.0*gt3/trials) + '%')
print('gt4:' + str(gt4)+ ' > ' + str(100.0*gt4/trials) + '%')
print('gt5:' + str(gt5))
print('gt6:' + str(gt6))
print('gt7:' + str(gt7))
