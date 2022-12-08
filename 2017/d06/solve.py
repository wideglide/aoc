#!/usr/bin/env python

d = [  l.strip().split('\t') for l in open('input','rb').readlines()] 

n = map(int,d[0])

def get_index(mem, val):
  maxi = [i for i,c in enumerate(mem) if c == val]
  return maxi


def redistribute(mem):
  maxv = max(mem)
  i = [i for i,c in enumerate(mem) if c == maxv][0]
  mem[i] = 0
  for v in range(maxv, 0, -1):
        i = (i + 1) % len(mem)
        mem[i] += 1
  return mem 

results = set()
win = ""

for i in xrange(1,99999):
  bank = redistribute(n)
  bstr = ''.join(map(str,bank))
  if bstr not in results :
    results.add(bstr)
  elif bstr == win:
    print part1, i-part1 
    break
  elif win == "":
    part1 = i
    win = bstr
    print win, i
  n = bank
