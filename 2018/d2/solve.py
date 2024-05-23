#!/usr/bin/evn python3
from itertools import groupby

d = open('input.txt','r').read().split()

two = three = 0
for l in d:
   l1 = [len(list(v)) for k,v in groupby(sorted(l))]
   if 2 in l1:  
     two += 1
   if 3 in l1: 
     three += 1
print( two * three)

for l1 in d:
    for l2 in d:
        eq = [ii[0]!=ii[1] for ii in zip(l1,l2) ]
        if sum(eq) == 1:
            print(''.join([ii[0] for ii in zip(l1,l2) if ii[0]==ii[1]]))
            quit()
