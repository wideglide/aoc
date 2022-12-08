from itertools import permutations
import sys

def readInput():
  d = {}
  for line  in open('input','rt').readlines():
    src,z,dst,z,dist = line.strip().split(" ")
    dist = int(dist)
    if src not in d:
      d[src] = {dst:dist}
      d[dst] = {src:dist}
    else:
      d[src][dst] = dist
  return d

table = readInput()
print(table.keys())
print(table.values())
#best = sys.maxint
best = 0
for p in permutations(table.keys()):
  curr = 0
  for i in range(len(p)-1):
    s = p[i]
    d = p[(i+1)]
    try:
      curr += table[s][d]
    except:
      curr += table[d][s]
  if curr > best:
    print(p)
  best = max(best,curr)
print(best)
