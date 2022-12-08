#!/usr/bin/env python

d = [  int(l.strip()) for l in open('input','rb').readlines()] 

i = 0
cnt = 0
while i >= 0 and i < len(d):
  v = d[i]
  if v >2:
    d[i] -= 1
  else:
    d[i] += 1
  i += v 
  cnt += 1
print cnt
