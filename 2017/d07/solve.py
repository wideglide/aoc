#!/usr/bin/env python

d = [  l.strip() for l in open('input','rb').readlines()] 

tower = dict()
weights = dict()
for l in d:
  if '->' in l:
    p0w, pn = l.split('->')
  else:
    p0w = l
  p0,w = p0w.split(' ')[:2] 
  w = int(w[1:-1])
  weights[p0.strip()] = [w]
  for child in pn.split(','):
    tower[child.strip()] = p0

for p in weights.keys():
  if p not in tower:
    print p    
  else:
    parent = tower[p]
    weights[parent].append(weights[p][0])

for p in weights.keys():
  if len(weights[p]) > 1:
    print len(weights[p]), weights[p]


