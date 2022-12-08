import re

def readInput():
  d = {}
  for line in open('input','rt').readlines():
    line = line.strip()
    dists = [int(s) for s in line.split() if s.isdigit()]
    alt = map(int,re.findall(r'\d+',line))
    reindeer = line.split()[0]
    d[reindeer] = dists
  return d

table = readInput()
time = 2503
for deer,v in table.items():
  rnd = time // (v[1]+v[2])
  dist = rnd * v[0] * v[1]
  if time < (rnd*(v[1]+v[2])+v[1]):
    dist += (time - (v[1]+v[2])*rnd)*v[0]
  print(deer,"flew",dist)

points = {}
for deer in table.keys():
  points[deer] = {'dist':0,'pts':0,'rest':0}

for i in range(2503):
    lead = -1
    for deer in points.keys():
      if points[deer]['rest'] > 0:
        points[deer]['dist'] += table[deer][0]
      if points[deer]['rest'] == table[deer][1]:
        points[deer]['rest'] = -table[deer][2]
      points[deer]['rest'] += 1
      if lead < points[deer]['dist']:
        lead = points[deer]['dist']
        leader = deer
    if leader:
      points[leader]['pts'] += 1

print(points.values())

