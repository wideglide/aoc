f = [ i.strip() for i in open('input').read().strip().split(',')]

pos = [0,0,0]
places = {(0,0):1}
for d in f:
  if d[0] == "R": pos[2] = (pos[2] + 1) % 4
  if d[0] == "L": pos[2] = (pos[2] - 1) % 4
  m = int(d[1:])
  for i in xrange(m):
      if pos[2] == 0: pos[1] += 1
      if pos[2] == 1: pos[0] += 1
      if pos[2] == 2: pos[1] -= 1
      if pos[2] == 3: pos[0] -= 1 
      
      if (pos[0],pos[1]) not in places:
        places[(pos[0],pos[1])] = 1
      else:
        print "part two = ", pos, abs(pos[0])+abs(pos[1])
print pos, abs(pos[0])+abs(pos[1])
