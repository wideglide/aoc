from itertools import permutations

def readInput():
  d = {}
  for line  in open('input','rt').readlines():
    name,z,op,num,z,z,z,z,z,z,neigh = line.strip()[:-1].split(" ")
    if op == 'lose':
      num = -int(num)
    else:
      num = int(num)
    if name not in d:
      d[name] = {neigh:num}
    else:
      d[name][neigh] = num
  return d

def addMe(d):
  d['Josh'] = {}
  for n in d.keys():
    d['Josh'][n] = 0
    d[n]['Josh'] = 0

table = readInput()
addMe(table)
best = 0
for p in permutations(table.keys()):
  curr = 0
  for i in range(len(p)):
    me = p[i]
    n1 = p[(i+1) % len(p)]
    n2 = p[i-1]
    curr += table[me][n1] + table[me][n2]
  best = max(best,curr)
print(best)
