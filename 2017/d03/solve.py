#!/usr/bin/env python
import math, sys 

myin = 312051 
#myin = 1024
# myin = 23

l = 1
w = 1
cnt = 0

while l  < myin:
  l += (cnt *8) 
  w = cnt * 2 + 1 
  cnt += 1
print "board", cnt, l, w


def part1(grid, w):
  i = w - 1 
  j = w - 1 
  for v in xrange(l, 0, -1):
    grid[j][i] = v
    if v == myin:
      print (i,j), v 
      print ( abs(i - (w//2 )) + abs(j -(w//2 )))
      break
    if j == 0:
      i += 1
    if i == 0:
      j -= 1
    if j == (w-1):
      i -= 1
    elif i == (w-1):
      j += 1 

def getsum(g, x, y, w):
  total = 0
  if y > 0 and x > 0:
    total += g[y-1][x-1]
  if y > 0:
    total += g[y-1][x]
  if y > 0 and x < w: 
    total += g[y-1][x+1]
  if x > 0:
    total += g[y][x-1]
  if x < w:
    total += g[y][x+1]
  if y < w and x > 0:
    total += g[y+1][x-1]
  if y< w:
    total += g[y+1][x]
  if y < w and  x < w:
    total += g[y+1][x+1]
  if total > myin:
    print (x,y), w, total
    sys.exit()
  return total

grid = [ [0] * w for item in xrange(w) ]  
print "grid", len(grid), len(grid[0])
c = w//2
grid[c][c] = 1 
for wid in xrange(3,w+1,2):
  x0 = c - wid//2
  y0 = c - wid//2
  x1 = (wid-1) 
  y1 = (wid-1) -1 
  for y1 in xrange(wid-2, -1, -1):
    grid[y0+y1][x0+x1] = getsum(grid, (x0+x1), (y0+y1), w-1 )
  for x1 in xrange(wid-2, -1, -1):
    grid[y0+y1][x0+x1] = getsum(grid, (x0+x1), (y0+y1), w-1 )
  for y1 in xrange(1, wid, 1):
    grid[y0+y1][x0+x1] = getsum(grid, (x0+x1), (y0+y1), w-1 )
  for x1 in xrange(1, wid, 1):
    grid[y0+y1][x0+x1] = getsum(grid, (x0+x1), (y0+y1), w-1 )

