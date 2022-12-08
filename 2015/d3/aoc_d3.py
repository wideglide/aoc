pos = (0,0)
d = {pos:1}


for c in open('INPUT','rt').read():
  if c == '^':
    pos = (pos[0],pos[1]+1)
  elif c == '>':
    pos = (pos[0]+1,pos[1])
  elif c == '<':
    pos = (pos[0]-1,pos[1])
  elif c == 'v':
    pos = (pos[0],pos[1]-1)
  d[pos] = 1
print(len(d))


p = [(0,0),(0,0)]
d = {p[0]:1}
i = 0

for c in open('INPUT','rt').read():
  if c == '^':
    p[i] = (p[i][0],p[i][1]+1)
  elif c == '>':
    p[i] = (p[i][0]+1,p[i][1])
  elif c == '<':
    p[i] = (p[i][0]-1,p[i][1])
  elif c == 'v':
    p[i] = (p[i][0],p[i][1]-1)
  d[p[i]] = 1
  i = i ^ 1
print(len(d))
