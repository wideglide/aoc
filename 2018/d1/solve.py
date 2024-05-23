#!/usr/bin/env python3

d = list(map(int, open('input.txt','r').read().split()))
print("N:",len(d))
r = sum(d)
print("ANS: ",r)
s = set()
f = 0
while f not in s:
  for i in d:
      if f in s:
          print("REPEAT:",f)
          break
      s.add(f)
      f += i
