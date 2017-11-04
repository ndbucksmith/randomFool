import numpy as np 
import random as rand 
sq = 16 
darts = 8
criterion = 3 
gt2 = gt3 = gt4 = gt1 = gt5 = gt6= gt7= 0 
trials =1000000 
bintots = np.zeros([sq]) 


def probprt(tag, valu):
    print(tag + ':'+ str(valu) + ' > ' + str(100.0*valu/trials) + '%') 

eqct12 = eqct23 = eqct13 = eqct123 = 0
for gg in range(trials):
    int1 =  int(rand.random() * sq )
    int2 =  int(rand.random() * sq )
    int3 =  int(rand.random() * sq )
    if int1 == int2:
        eqct12 +=1
    if int3 == int2:
        eqct23 +=1       
    if int3 == int1:
        eqct13 +=1         
    if int3 == int1  and int3 == int2:
        eqct123 +=1              
probprt('eqct12', eqct12)
probprt('eqct13', eqct13)
probprt('eqct23', eqct23)
probprt('eqct123', eqct123)

for jj in range(trials): 
        bins = np.zeros([sq]) 
        for kk in range(darts): 
            posi = rand.random() * sq 
            bintots[int(posi)] +=1 
            bins[int(posi)] +=1 
        for hh in range(sq): 
           if bins[hh] > 7: 
               gt7 +=1 
           elif bins[hh] > 6: 
               gt6 +=1 
           elif bins[hh] > 5: 
               gt5 +=1 
           elif bins[hh] > 4: 
               gt4 +=1 
           elif bins[hh] > 3: 
               gt3 +=1 
           elif bins[hh] > 2: 
               gt2 +=1
           elif bins[hh] > 1: 
               gt1 +=1

print('coun in each bin')
print(bintots) 
probprt('gt1:', gt1) 
probprt('gt2:', gt2) 
probprt('gt3:', gt3) 
probprt('gt4:', gt4) 
probprt('gt5:', gt5) 
probprt('gt6:', gt6) 
probprt('gt7:', gt7) 