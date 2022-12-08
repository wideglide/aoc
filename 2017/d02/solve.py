#!/usr/bin/env python
import itertools

d = [ map(int, l.strip().split('\t')) for l in open('input','rb').readlines()] 


checksum = sum( [ max(l) - min(l) for l in d ])
print checksum

checksum = 0
for l in d:
  for i in xrange(len(l)):
    for j in xrange(len(l)):
      if l[i] % l[j] == 0 and i != j: 
        checksum += max( (l[i], l[j]) ) / min( (l[i], l[j]) )
print checksum

checksum = 0
for l in d:
  for c in itertools.combinations(l,2):
    if c[0] % c[1] == 0 and c[0] != c[1]:
      checksum += max(c) / min(c)
print checksum 
